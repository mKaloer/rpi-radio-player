import logging

from mpd import MPDClient


_player = MPDClient()
_player.connect("localhost", 6600)

def play_url(url):
    _player.load(url)
    _player.play(0)


def play():
    _player.pause(0)


def pause():
    _player.pause(1)


def stop():
    _player.stop()
