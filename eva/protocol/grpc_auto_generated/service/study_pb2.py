# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: study.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='study.proto',
  package='service.study',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bstudy.proto\x12\rservice.study\",\n\x19MoveToPreviousWordRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"/\n\x1aMoveToPreviousWordResponse\x12\x11\n\tnew_index\x18\x01 \x01(\x05\"(\n\x15MoveToNextWordRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"+\n\x16MoveToNextWordResponse\x12\x11\n\tnew_index\x18\x01 \x01(\x05\x32\xd5\x01\n\x05Study\x12k\n\x12MoveToPreviousWord\x12(.service.study.MoveToPreviousWordRequest\x1a).service.study.MoveToPreviousWordResponse\"\x00\x12_\n\x0eMoveToNextWord\x12$.service.study.MoveToNextWordRequest\x1a%.service.study.MoveToNextWordResponse\"\x00\x62\x06proto3')
)




_MOVETOPREVIOUSWORDREQUEST = _descriptor.Descriptor(
  name='MoveToPreviousWordRequest',
  full_name='service.study.MoveToPreviousWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='service.study.MoveToPreviousWordRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=74,
)


_MOVETOPREVIOUSWORDRESPONSE = _descriptor.Descriptor(
  name='MoveToPreviousWordResponse',
  full_name='service.study.MoveToPreviousWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_index', full_name='service.study.MoveToPreviousWordResponse.new_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=123,
)


_MOVETONEXTWORDREQUEST = _descriptor.Descriptor(
  name='MoveToNextWordRequest',
  full_name='service.study.MoveToNextWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='service.study.MoveToNextWordRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=165,
)


_MOVETONEXTWORDRESPONSE = _descriptor.Descriptor(
  name='MoveToNextWordResponse',
  full_name='service.study.MoveToNextWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_index', full_name='service.study.MoveToNextWordResponse.new_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=210,
)

DESCRIPTOR.message_types_by_name['MoveToPreviousWordRequest'] = _MOVETOPREVIOUSWORDREQUEST
DESCRIPTOR.message_types_by_name['MoveToPreviousWordResponse'] = _MOVETOPREVIOUSWORDRESPONSE
DESCRIPTOR.message_types_by_name['MoveToNextWordRequest'] = _MOVETONEXTWORDREQUEST
DESCRIPTOR.message_types_by_name['MoveToNextWordResponse'] = _MOVETONEXTWORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MoveToPreviousWordRequest = _reflection.GeneratedProtocolMessageType('MoveToPreviousWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOPREVIOUSWORDREQUEST,
  '__module__' : 'study_pb2'
  # @@protoc_insertion_point(class_scope:service.study.MoveToPreviousWordRequest)
  })
_sym_db.RegisterMessage(MoveToPreviousWordRequest)

MoveToPreviousWordResponse = _reflection.GeneratedProtocolMessageType('MoveToPreviousWordResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOPREVIOUSWORDRESPONSE,
  '__module__' : 'study_pb2'
  # @@protoc_insertion_point(class_scope:service.study.MoveToPreviousWordResponse)
  })
_sym_db.RegisterMessage(MoveToPreviousWordResponse)

MoveToNextWordRequest = _reflection.GeneratedProtocolMessageType('MoveToNextWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVETONEXTWORDREQUEST,
  '__module__' : 'study_pb2'
  # @@protoc_insertion_point(class_scope:service.study.MoveToNextWordRequest)
  })
_sym_db.RegisterMessage(MoveToNextWordRequest)

MoveToNextWordResponse = _reflection.GeneratedProtocolMessageType('MoveToNextWordResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVETONEXTWORDRESPONSE,
  '__module__' : 'study_pb2'
  # @@protoc_insertion_point(class_scope:service.study.MoveToNextWordResponse)
  })
_sym_db.RegisterMessage(MoveToNextWordResponse)



_STUDY = _descriptor.ServiceDescriptor(
  name='Study',
  full_name='service.study.Study',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=213,
  serialized_end=426,
  methods=[
  _descriptor.MethodDescriptor(
    name='MoveToPreviousWord',
    full_name='service.study.Study.MoveToPreviousWord',
    index=0,
    containing_service=None,
    input_type=_MOVETOPREVIOUSWORDREQUEST,
    output_type=_MOVETOPREVIOUSWORDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MoveToNextWord',
    full_name='service.study.Study.MoveToNextWord',
    index=1,
    containing_service=None,
    input_type=_MOVETONEXTWORDREQUEST,
    output_type=_MOVETONEXTWORDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDY)

DESCRIPTOR.services_by_name['Study'] = _STUDY

# @@protoc_insertion_point(module_scope)
