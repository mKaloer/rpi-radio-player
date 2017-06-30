import logging
import threading

from mpd import MPDClient, ConnectionError

logger = logging.getLogger(__name__)

def autoconnect():
    def autoconnect_decorator(func):
        def func_wrapper(self, *args, **kwargs):
            self._ensure_connected()
            return func(self, *args, **kwargs)
        return func_wrapper
    return autoconnect_decorator

class Radio():

    def __init__(self):
        self._player = MPDClient()
        self._observers = set()
        self._event_thread = None
        self._check_events = False
        self._event_thread_lock = threading.Lock()

    def _connect(self):
        self._player.connect("localhost", 6600)


    def _ensure_connected(self):
        try:
            self._player.ping()
        except BrokenPipeError:
            logger.warning("Broken pipe: Recreating client")
            self._player = MPDClient()
            self._connect()
        except ConnectionError:
            logger.warning("Connection error: Reconnecting...")
            self._connect()


    @autoconnect()
    def play_url(self, url):
        logger.info("Playing URL: %s", url)
        self._player.clear()
        self._player.load(url)
        self._player.play(0)


    @autoconnect()
    def play(self):
        logger.info("Playing")
        self._player.pause(0)


    @autoconnect()
    def pause(self):
        logger.info("Pausing")
        self._player.pause(1)

    @autoconnect()
    def stop(self):
        logger.info("Stopping")
        self._player.stop()


    @autoconnect()
    def set_volume(self, volume):
        if volume > 100 or volume < 0:
            raise ValueError("Volume must be between 0 and 100")
        logger.info("Setting volume")
        self._player.setvol(volume)


    @autoconnect()
    def get_status(self):
        logger.info("Get status")
        track_status = self._player.currentsong()
        player_status = self._player.status()
        return {
            'title': track_status.get('title'),
            'name': track_status.get('name'),
            'volume': player_status.get('volume'),
            'bitrate': player_status.get('bitrate'),
            'state': player_status.get('state')
        }


    def register_event_listener(self, event_method):
        if self._event_thread is None or (not self._event_thread.is_alive()):
            # Start thread
            self._start_event_thread()
        with self._event_thread_lock:
            self._observers.add(event_method)


    def unregister_event_listener(self, event_method):
        with self._event_thread_lock:
            self._observers.remove(event_method)
        if len(self._observers) == 0:
            self._stop_event_thread()


    def _listen_for_updates(self, logger):
        # Create radio instance for events (MPDClient is not thread safe)
        event_radio = Radio()
        while self._check_events:
            event_radio._ensure_connected()
            updates = event_radio._player.idle()
            if len(updates) > 0:
                logger.debug("Received update from mpd")
                status = event_radio.get_status()
                with self._event_thread_lock:
                    for observer in self._observers:
                        try:
                            observer(status)
                        except:
                            logger.warning("Error invoking observer", exc_info=True)


    @autoconnect()
    def _start_event_thread(self):
        with self._event_thread_lock:
            self._check_events = True
        self._event_thread = threading.Thread(target=self._listen_for_updates, args=(logger,))
        logger.info("Starting event thread")
        self._event_thread.start()


    def _stop_event_thread(self):
        with self._event_thread_lock:
            self._check_events = False
            logger.info("Stopping event thread")
            self._player.noidle()
        self._event_thread.join()
