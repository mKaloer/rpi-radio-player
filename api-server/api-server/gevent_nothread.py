import sys
_socket = __import__("socket")

import gevent
from gevent.socket import wait_write, socket

import gunicorn.workers.ggevent as ggevent
from gunicorn.workers.ggevent import GeventWorker


class GeventWorkerNoThreadPatch(GeventWorker):

    def patch(self):
        from gevent import monkey
        monkey.noisy = False

        # if the new version is used make sure to patch subprocess
        if gevent.version_info[0] == 0:
            monkey.patch_all(thread=False)
        else:
            monkey.patch_all(thread=False, subprocess=True)

        from psycogreen.gevent import patch_psycopg
        patch_psycopg()

        # monkey patch sendfile to make it none blocking
        ggevent.patch_sendfile()

        # patch sockets
        sockets = []
        for s in self.sockets:
            if sys.version_info[0] == 3:
                sockets.append(socket(s.FAMILY, _socket.SOCK_STREAM,
                    fileno=s.sock.fileno()))
            else:
                sockets.append(socket(s.FAMILY, _socket.SOCK_STREAM,
                    _sock=s))
        self.sockets = sockets
