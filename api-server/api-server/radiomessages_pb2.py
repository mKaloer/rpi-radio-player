# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: radiomessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='radiomessages.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x13radiomessages.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1a\n\x0bPlayRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1f\n\rVolumeRequest\x12\x0e\n\x06volume\x18\x01 \x01(\x05\"\xaf\x01\n\x0eStatusResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12$\n\x05state\x18\x02 \x01(\x0e\x32\x15.StatusResponse.State\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06volume\x18\x05 \x01(\x05\x12\x0f\n\x07\x62itrate\x18\x06 \x01(\x05\",\n\x05State\x12\x0b\n\x07PLAYING\x10\x00\x12\x0b\n\x07STOPPED\x10\x01\x12\t\n\x05MUTED\x10\x02\x32\xc9\x02\n\x05Radio\x12%\n\x04Play\x12\x0c.PlayRequest\x1a\x0f.StatusResponse\x12/\n\x04Stop\x12\x16.google.protobuf.Empty\x1a\x0f.StatusResponse\x12\x31\n\x06Status\x12\x16.google.protobuf.Empty\x1a\x0f.StatusResponse\x12,\n\tSetVolume\x12\x0e.VolumeRequest\x1a\x0f.StatusResponse\x12?\n\x12SubscribeToUpdates\x12\x16.google.protobuf.Empty\x1a\x0f.StatusResponse0\x01\x12\x46\n\x14UnsubscribeToUpdates\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Emptyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STATUSRESPONSE_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='StatusResponse.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAYING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUTED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=245,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_STATUSRESPONSE_STATE)


_PLAYREQUEST = _descriptor.Descriptor(
  name='PlayRequest',
  full_name='PlayRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='PlayRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=78,
)


_VOLUMEREQUEST = _descriptor.Descriptor(
  name='VolumeRequest',
  full_name='VolumeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='volume', full_name='VolumeRequest.volume', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=111,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='StatusResponse.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='StatusResponse.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='StatusResponse.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='StatusResponse.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='StatusResponse.volume', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bitrate', full_name='StatusResponse.bitrate', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUSRESPONSE_STATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=289,
)

_STATUSRESPONSE.fields_by_name['state'].enum_type = _STATUSRESPONSE_STATE
_STATUSRESPONSE_STATE.containing_type = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['PlayRequest'] = _PLAYREQUEST
DESCRIPTOR.message_types_by_name['VolumeRequest'] = _VOLUMEREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE

PlayRequest = _reflection.GeneratedProtocolMessageType('PlayRequest', (_message.Message,), dict(
  DESCRIPTOR = _PLAYREQUEST,
  __module__ = 'radiomessages_pb2'
  # @@protoc_insertion_point(class_scope:PlayRequest)
  ))
_sym_db.RegisterMessage(PlayRequest)

VolumeRequest = _reflection.GeneratedProtocolMessageType('VolumeRequest', (_message.Message,), dict(
  DESCRIPTOR = _VOLUMEREQUEST,
  __module__ = 'radiomessages_pb2'
  # @@protoc_insertion_point(class_scope:VolumeRequest)
  ))
_sym_db.RegisterMessage(VolumeRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'radiomessages_pb2'
  # @@protoc_insertion_point(class_scope:StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class RadioStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Play = channel.unary_unary(
          '/Radio/Play',
          request_serializer=PlayRequest.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.Stop = channel.unary_unary(
          '/Radio/Stop',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.Status = channel.unary_unary(
          '/Radio/Status',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.SetVolume = channel.unary_unary(
          '/Radio/SetVolume',
          request_serializer=VolumeRequest.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.SubscribeToUpdates = channel.unary_stream(
          '/Radio/SubscribeToUpdates',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=StatusResponse.FromString,
          )
      self.UnsubscribeToUpdates = channel.unary_unary(
          '/Radio/UnsubscribeToUpdates',
          request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
          response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
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

    def SetVolume(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def SubscribeToUpdates(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def UnsubscribeToUpdates(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_RadioServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Play': grpc.unary_unary_rpc_method_handler(
            servicer.Play,
            request_deserializer=PlayRequest.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'Stop': grpc.unary_unary_rpc_method_handler(
            servicer.Stop,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'Status': grpc.unary_unary_rpc_method_handler(
            servicer.Status,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'SetVolume': grpc.unary_unary_rpc_method_handler(
            servicer.SetVolume,
            request_deserializer=VolumeRequest.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'SubscribeToUpdates': grpc.unary_stream_rpc_method_handler(
            servicer.SubscribeToUpdates,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=StatusResponse.SerializeToString,
        ),
        'UnsubscribeToUpdates': grpc.unary_unary_rpc_method_handler(
            servicer.UnsubscribeToUpdates,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Radio', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaRadioServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Play(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Stop(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Status(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SetVolume(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def SubscribeToUpdates(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def UnsubscribeToUpdates(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaRadioStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Play(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Play.future = None
    def Stop(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Stop.future = None
    def Status(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Status.future = None
    def SetVolume(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    SetVolume.future = None
    def SubscribeToUpdates(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    def UnsubscribeToUpdates(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    UnsubscribeToUpdates.future = None


  def beta_create_Radio_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Radio', 'Play'): PlayRequest.FromString,
      ('Radio', 'SetVolume'): VolumeRequest.FromString,
      ('Radio', 'Status'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('Radio', 'Stop'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('Radio', 'SubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
      ('Radio', 'UnsubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    response_serializers = {
      ('Radio', 'Play'): StatusResponse.SerializeToString,
      ('Radio', 'SetVolume'): StatusResponse.SerializeToString,
      ('Radio', 'Status'): StatusResponse.SerializeToString,
      ('Radio', 'Stop'): StatusResponse.SerializeToString,
      ('Radio', 'SubscribeToUpdates'): StatusResponse.SerializeToString,
      ('Radio', 'UnsubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    method_implementations = {
      ('Radio', 'Play'): face_utilities.unary_unary_inline(servicer.Play),
      ('Radio', 'SetVolume'): face_utilities.unary_unary_inline(servicer.SetVolume),
      ('Radio', 'Status'): face_utilities.unary_unary_inline(servicer.Status),
      ('Radio', 'Stop'): face_utilities.unary_unary_inline(servicer.Stop),
      ('Radio', 'SubscribeToUpdates'): face_utilities.unary_stream_inline(servicer.SubscribeToUpdates),
      ('Radio', 'UnsubscribeToUpdates'): face_utilities.unary_unary_inline(servicer.UnsubscribeToUpdates),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Radio_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Radio', 'Play'): PlayRequest.SerializeToString,
      ('Radio', 'SetVolume'): VolumeRequest.SerializeToString,
      ('Radio', 'Status'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('Radio', 'Stop'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('Radio', 'SubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ('Radio', 'UnsubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    }
    response_deserializers = {
      ('Radio', 'Play'): StatusResponse.FromString,
      ('Radio', 'SetVolume'): StatusResponse.FromString,
      ('Radio', 'Status'): StatusResponse.FromString,
      ('Radio', 'Stop'): StatusResponse.FromString,
      ('Radio', 'SubscribeToUpdates'): StatusResponse.FromString,
      ('Radio', 'UnsubscribeToUpdates'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    }
    cardinalities = {
      'Play': cardinality.Cardinality.UNARY_UNARY,
      'SetVolume': cardinality.Cardinality.UNARY_UNARY,
      'Status': cardinality.Cardinality.UNARY_UNARY,
      'Stop': cardinality.Cardinality.UNARY_UNARY,
      'SubscribeToUpdates': cardinality.Cardinality.UNARY_STREAM,
      'UnsubscribeToUpdates': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Radio', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
