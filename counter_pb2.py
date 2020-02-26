# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: counter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='counter.proto',
  package='demo.counter',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rcounter.proto\x12\x0c\x64\x65mo.counter\"\x1e\n\x0e\x43ounterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\x0c\x43ounterReply\x12\r\n\x05\x63ount\x18\x01 \x01(\t2\x90\x01\n\x07\x43ounter\x12\x42\n\x04incr\x12\x1c.demo.counter.CounterRequest\x1a\x1a.demo.counter.CounterReply\"\x00\x12\x41\n\x03get\x12\x1c.demo.counter.CounterRequest\x1a\x1a.demo.counter.CounterReply\"\x00\x62\x06proto3'
)




_COUNTERREQUEST = _descriptor.Descriptor(
  name='CounterRequest',
  full_name='demo.counter.CounterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='demo.counter.CounterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=31,
  serialized_end=61,
)


_COUNTERREPLY = _descriptor.Descriptor(
  name='CounterReply',
  full_name='demo.counter.CounterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='demo.counter.CounterReply.count', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=63,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['CounterRequest'] = _COUNTERREQUEST
DESCRIPTOR.message_types_by_name['CounterReply'] = _COUNTERREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CounterRequest = _reflection.GeneratedProtocolMessageType('CounterRequest', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERREQUEST,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:demo.counter.CounterRequest)
  })
_sym_db.RegisterMessage(CounterRequest)

CounterReply = _reflection.GeneratedProtocolMessageType('CounterReply', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERREPLY,
  '__module__' : 'counter_pb2'
  # @@protoc_insertion_point(class_scope:demo.counter.CounterReply)
  })
_sym_db.RegisterMessage(CounterReply)



_COUNTER = _descriptor.ServiceDescriptor(
  name='Counter',
  full_name='demo.counter.Counter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=95,
  serialized_end=239,
  methods=[
  _descriptor.MethodDescriptor(
    name='incr',
    full_name='demo.counter.Counter.incr',
    index=0,
    containing_service=None,
    input_type=_COUNTERREQUEST,
    output_type=_COUNTERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='demo.counter.Counter.get',
    index=1,
    containing_service=None,
    input_type=_COUNTERREQUEST,
    output_type=_COUNTERREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COUNTER)

DESCRIPTOR.services_by_name['Counter'] = _COUNTER

# @@protoc_insertion_point(module_scope)
