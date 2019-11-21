# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='service.test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntest.proto\x12\x0cservice.test\"\x1f\n\x0cIKnowRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\"\n\rIKnowResponse\x12\x11\n\tnew_index\x18\x01 \x01(\x05\"#\n\x10IDontKnowRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"&\n\x11IDontKnowResponse\x12\x11\n\tnew_index\x18\x01 \x01(\x05\x32\x9a\x01\n\x04Test\x12\x42\n\x05IKnow\x12\x1a.service.test.IKnowRequest\x1a\x1b.service.test.IKnowResponse\"\x00\x12N\n\tIDontKnow\x12\x1e.service.test.IDontKnowRequest\x1a\x1f.service.test.IDontKnowResponse\"\x00\x62\x06proto3')
)




_IKNOWREQUEST = _descriptor.Descriptor(
  name='IKnowRequest',
  full_name='service.test.IKnowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='service.test.IKnowRequest.user_id', index=0,
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
  serialized_start=28,
  serialized_end=59,
)


_IKNOWRESPONSE = _descriptor.Descriptor(
  name='IKnowResponse',
  full_name='service.test.IKnowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_index', full_name='service.test.IKnowResponse.new_index', index=0,
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
  serialized_start=61,
  serialized_end=95,
)


_IDONTKNOWREQUEST = _descriptor.Descriptor(
  name='IDontKnowRequest',
  full_name='service.test.IDontKnowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='service.test.IDontKnowRequest.user_id', index=0,
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
  serialized_start=97,
  serialized_end=132,
)


_IDONTKNOWRESPONSE = _descriptor.Descriptor(
  name='IDontKnowResponse',
  full_name='service.test.IDontKnowResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_index', full_name='service.test.IDontKnowResponse.new_index', index=0,
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
  serialized_start=134,
  serialized_end=172,
)

DESCRIPTOR.message_types_by_name['IKnowRequest'] = _IKNOWREQUEST
DESCRIPTOR.message_types_by_name['IKnowResponse'] = _IKNOWRESPONSE
DESCRIPTOR.message_types_by_name['IDontKnowRequest'] = _IDONTKNOWREQUEST
DESCRIPTOR.message_types_by_name['IDontKnowResponse'] = _IDONTKNOWRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IKnowRequest = _reflection.GeneratedProtocolMessageType('IKnowRequest', (_message.Message,), {
  'DESCRIPTOR' : _IKNOWREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:service.test.IKnowRequest)
  })
_sym_db.RegisterMessage(IKnowRequest)

IKnowResponse = _reflection.GeneratedProtocolMessageType('IKnowResponse', (_message.Message,), {
  'DESCRIPTOR' : _IKNOWRESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:service.test.IKnowResponse)
  })
_sym_db.RegisterMessage(IKnowResponse)

IDontKnowRequest = _reflection.GeneratedProtocolMessageType('IDontKnowRequest', (_message.Message,), {
  'DESCRIPTOR' : _IDONTKNOWREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:service.test.IDontKnowRequest)
  })
_sym_db.RegisterMessage(IDontKnowRequest)

IDontKnowResponse = _reflection.GeneratedProtocolMessageType('IDontKnowResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDONTKNOWRESPONSE,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:service.test.IDontKnowResponse)
  })
_sym_db.RegisterMessage(IDontKnowResponse)



_TEST = _descriptor.ServiceDescriptor(
  name='Test',
  full_name='service.test.Test',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=175,
  serialized_end=329,
  methods=[
  _descriptor.MethodDescriptor(
    name='IKnow',
    full_name='service.test.Test.IKnow',
    index=0,
    containing_service=None,
    input_type=_IKNOWREQUEST,
    output_type=_IKNOWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IDontKnow',
    full_name='service.test.Test.IDontKnow',
    index=1,
    containing_service=None,
    input_type=_IDONTKNOWREQUEST,
    output_type=_IDONTKNOWRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEST)

DESCRIPTOR.services_by_name['Test'] = _TEST

# @@protoc_insertion_point(module_scope)