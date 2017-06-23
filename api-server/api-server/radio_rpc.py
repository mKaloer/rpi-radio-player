from concurrent import futures
from enum import Enum
import logging
import threading

import grpc

import radiomessages_pb2
import radiomessages_pb2_grpc
from google.protobuf import empty_pb2


logger = logging.getLogger(__name__)


class RadioRPC():
    """
    Class for invoking RPCs for the radio service.
    """

    def __init__(self, host):
        logger.info("Connecting to grpc channel")
        self.channel = grpc.insecure_channel(host)
        self.stub = radiomessages_pb2_grpc.RadioStub(self.channel)
        self._listener_threads = {}

    def play(self, url=None):
        try:
            logger.debug("Sending play request")
            response = self.stub.Play(radiomessages_pb2.PlayRequest(url=url))
            return RadioRPC._format_status(response)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(e.details())
            else:
                raise


    def stop(self):
        logger.debug("Sending stop request")
        return RadioRPC._format_status(self.stub.Stop(empty_pb2.Empty()))


    def get_status(self):
        logger.debug("Sending get status request")
        return RadioRPC._format_status(self.stub.Status(empty_pb2.Empty()))


    def subscribe_to_updates(self, listener):
        logger.debug("Subscribing to updates")
        def async_listener():
            for status in self.stub.SubscribeToUpdates(empty_pb2.Empty()):
                if status:
                    listener(RadioRPC._format_status(status))

        t = threading.Thread(target=async_listener)
        t.start()
        self._listener_threads[listener] = t


    def unsubscribe_to_updates(self, listener):
        self.stub.UnsubscribeToUpdates(empty_pb2.Empty())
        if listener in self._listener_threads:
            self._listener_threads[listener].join()


    @staticmethod
    def _format_status(status):
        """
        Converts a format into a generic dict representation
        """
        return {
            'url': status.url,
            'state': RadioState(status.state),
            'title': status.title,
            'name': status.name,
            'volume': status.volume,
            'bitrate': status.bitrate,
        }


class RadioState(Enum):
    PLAYING = 0
    STOPPED = 1
    MUTED = 2
