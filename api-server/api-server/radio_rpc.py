from enum import Enum

import grpc

import radiomessages_pb2
import radiomessages_pb2_grpc
from google.protobuf import empty_pb2

class RadioRPC():
    """
    Class for invoking RPCs for the radio service.
    """

    def __init__(self, host):
        self.channel = grpc.insecure_channel(host)
        self.stub = radiomessages_pb2_grpc.RadioStub(self.channel)


    def play(self, url=None):
        try:
            response = self.stub.Play(radiomessages_pb2.PlayRequest(url=url))
            return RadioRPC._format_status(response)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(e.details())
            else:
                raise


    def stop(self):
        return RadioRPC._format_status(self.stub.Stop(empty_pb2.Empty()))


    def get_status(self):
        return RadioRPC._format_status(self.stub.Status(empty_pb2.Empty()))


    @staticmethod
    def _format_status(status):
        """
        Converts a format into a generic dict representation
        """
        return {
            'url': status.url,
            'state': RadioState(status.state)
        }


class RadioState(Enum):
    PLAYING = 0
    STOPPED = 1
    MUTED = 2
