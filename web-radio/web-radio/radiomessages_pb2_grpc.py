# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
import radiomessages_pb2 as radiomessages__pb2


class RadioStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Play = channel.unary_unary(
        '/Radio/Play',
        request_serializer=radiomessages__pb2.PlayRequest.SerializeToString,
        response_deserializer=radiomessages__pb2.StatusResponse.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Radio/Stop',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=radiomessages__pb2.StatusResponse.FromString,
        )
    self.Status = channel.unary_unary(
        '/Radio/Status',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=radiomessages__pb2.StatusResponse.FromString,
        )


class RadioServicer(object):

  def Play(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Status(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RadioServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Play': grpc.unary_unary_rpc_method_handler(
          servicer.Play,
          request_deserializer=radiomessages__pb2.PlayRequest.FromString,
          response_serializer=radiomessages__pb2.StatusResponse.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=radiomessages__pb2.StatusResponse.SerializeToString,
      ),
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=radiomessages__pb2.StatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Radio', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
