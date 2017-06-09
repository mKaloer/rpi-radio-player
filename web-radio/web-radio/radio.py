import logging

from mpd import MPDClient


_player = MPDClient()
_player.connect("localhost", 6600)

def play_url(url):
    _player.load(url)
    _player.play(0)
