# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_set.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_set.proto',
  package='artifacts.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0fimage_set.proto\x12\x0f\x61rtifacts.proto\"0\n\x12ImageSetMetaRecord\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"Q\n\x0eImageSetRecord\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x31\n\x04meta\x18\x02 \x03(\x0b\x32#.artifacts.proto.ImageSetMetaRecordb\x06proto3')
)




_IMAGESETMETARECORD = _descriptor.Descriptor(
  name='ImageSetMetaRecord',
  full_name='artifacts.proto.ImageSetMetaRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='artifacts.proto.ImageSetMetaRecord.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='artifacts.proto.ImageSetMetaRecord.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=84,
)


_IMAGESETRECORD = _descriptor.Descriptor(
  name='ImageSetRecord',
  full_name='artifacts.proto.ImageSetRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='artifacts.proto.ImageSetRecord.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meta', full_name='artifacts.proto.ImageSetRecord.meta', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=86,
  serialized_end=167,
)

_IMAGESETRECORD.fields_by_name['meta'].message_type = _IMAGESETMETARECORD
DESCRIPTOR.message_types_by_name['ImageSetMetaRecord'] = _IMAGESETMETARECORD
DESCRIPTOR.message_types_by_name['ImageSetRecord'] = _IMAGESETRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageSetMetaRecord = _reflection.GeneratedProtocolMessageType('ImageSetMetaRecord', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESETMETARECORD,
  __module__ = 'image_set_pb2'
  # @@protoc_insertion_point(class_scope:artifacts.proto.ImageSetMetaRecord)
  ))
_sym_db.RegisterMessage(ImageSetMetaRecord)

ImageSetRecord = _reflection.GeneratedProtocolMessageType('ImageSetRecord', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESETRECORD,
  __module__ = 'image_set_pb2'
  # @@protoc_insertion_point(class_scope:artifacts.proto.ImageSetRecord)
  ))
_sym_db.RegisterMessage(ImageSetRecord)


# @@protoc_insertion_point(module_scope)
