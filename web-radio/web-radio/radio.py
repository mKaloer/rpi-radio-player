import logging

from mpd import MPDClient, ConnectionError

def autoconnect():
    def autoconnect_decorator(func):
        def func_wrapper(self, *args, **kwargs):
            try:
                self._player.ping()
            except BrokenPipeError:
                self._player = MPDClient()
                self._connect()
            except ConnectionError:
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
        self._player.clear()
        self._player.load(url)
        self._player.play(0)


    @autoconnect()
    def play(self):
        self._player.pause(0)


    @autoconnect()
    def pause(self):
        self._player.pause(1)


    @autoconnect()
    def stop(self):
        self._player.stop()
