import logging

from mpd import MPDClient, ConnectionError

logger = logging.getLogger(__name__)

def autoconnect():
    def autoconnect_decorator(func):
        def func_wrapper(self, *args, **kwargs):
            try:
                self._player.ping()
            except BrokenPipeError:
                logger.warning("Broken pipe: Recreating client")
                self._player = MPDClient()
                self._connect()
            except ConnectionError:
                logger.warning("Connection error: Reconnecting...")
                self._connect()
            return func(self, *args, **kwargs)
        return func_wrapper
    return autoconnect_decorator

class Radio():

    def __init__(self):
        self._player = MPDClient()

    def _connect(self):
        self._player.connect("localhost", 6600)


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
