# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nuser.proto\x12\x04user\"\x14\n\x04Time\x12\x0c\n\x04time\x18\x01 \x01(\x03\"1\n\x0cStudyingWord\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rstudied_count\x18\x02 \x01(\x05\"U\n\x0bTestingWord\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0cpassed_count\x18\x02 \x01(\x05\x12$\n\x10last_passed_time\x18\x03 \x01(\x0b\x32\n.user.Time\";\n\rStudyingWords\x12*\n\x0estudying_words\x18\x01 \x03(\x0b\x32\x12.user.StudyingWord\"9\n\x0cTestingWords\x12)\n\x0estudying_words\x18\x01 \x03(\x0b\x32\x11.user.TestingWord\"\xca\x05\n\x04User\x12%\n\x11last_signing_time\x18\x01 \x01(\x0b\x32\n.user.Time\x12\x18\n\x10today_study_date\x18\x02 \x01(\x05\x12\x1c\n\x14last_studied_word_id\x18\x03 \x01(\x05\x12\x35\n\x0estudying_words\x18\x04 \x03(\x0b\x32\x1d.user.User.StudyingWordsEntry\x12\x33\n\rtesting_words\x18\x05 \x03(\x0b\x32\x1c.user.User.TestingWordsEntry\x12\"\n\x1atoday_studying_words_index\x18\x06 \x01(\x05\x12@\n\x14today_studying_words\x18\x07 \x03(\x0b\x32\".user.User.TodayStudyingWordsEntry\x12!\n\x19today_testing_words_index\x18\x08 \x01(\x05\x12>\n\x13today_testing_words\x18\t \x03(\x0b\x32!.user.User.TodayTestingWordsEntry\x1aH\n\x12StudyingWordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.user.StudyingWord:\x02\x38\x01\x1a\x46\n\x11TestingWordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.user.TestingWord:\x02\x38\x01\x1aN\n\x17TodayStudyingWordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.user.StudyingWords:\x02\x38\x01\x1aL\n\x16TodayTestingWordsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.user.TestingWords:\x02\x38\x01\x62\x06proto3')
)




_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='user.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='user.Time.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=20,
  serialized_end=40,
)


_STUDYINGWORD = _descriptor.Descriptor(
  name='StudyingWord',
  full_name='user.StudyingWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.StudyingWord.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studied_count', full_name='user.StudyingWord.studied_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=42,
  serialized_end=91,
)


_TESTINGWORD = _descriptor.Descriptor(
  name='TestingWord',
  full_name='user.TestingWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.TestingWord.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passed_count', full_name='user.TestingWord.passed_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_passed_time', full_name='user.TestingWord.last_passed_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=93,
  serialized_end=178,
)


_STUDYINGWORDS = _descriptor.Descriptor(
  name='StudyingWords',
  full_name='user.StudyingWords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='studying_words', full_name='user.StudyingWords.studying_words', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=180,
  serialized_end=239,
)


_TESTINGWORDS = _descriptor.Descriptor(
  name='TestingWords',
  full_name='user.TestingWords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='studying_words', full_name='user.TestingWords.studying_words', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=241,
  serialized_end=298,
)


_USER_STUDYINGWORDSENTRY = _descriptor.Descriptor(
  name='StudyingWordsEntry',
  full_name='user.User.StudyingWordsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='user.User.StudyingWordsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='user.User.StudyingWordsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=785,
)

_USER_TESTINGWORDSENTRY = _descriptor.Descriptor(
  name='TestingWordsEntry',
  full_name='user.User.TestingWordsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='user.User.TestingWordsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='user.User.TestingWordsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=787,
  serialized_end=857,
)

_USER_TODAYSTUDYINGWORDSENTRY = _descriptor.Descriptor(
  name='TodayStudyingWordsEntry',
  full_name='user.User.TodayStudyingWordsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='user.User.TodayStudyingWordsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='user.User.TodayStudyingWordsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=859,
  serialized_end=937,
)

_USER_TODAYTESTINGWORDSENTRY = _descriptor.Descriptor(
  name='TodayTestingWordsEntry',
  full_name='user.User.TodayTestingWordsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='user.User.TodayTestingWordsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='user.User.TodayTestingWordsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=939,
  serialized_end=1015,
)

_USER = _descriptor.Descriptor(
  name='User',
  full_name='user.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_signing_time', full_name='user.User.last_signing_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='today_study_date', full_name='user.User.today_study_date', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_studied_word_id', full_name='user.User.last_studied_word_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studying_words', full_name='user.User.studying_words', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='testing_words', full_name='user.User.testing_words', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='today_studying_words_index', full_name='user.User.today_studying_words_index', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='today_studying_words', full_name='user.User.today_studying_words', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='today_testing_words_index', full_name='user.User.today_testing_words_index', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='today_testing_words', full_name='user.User.today_testing_words', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USER_STUDYINGWORDSENTRY, _USER_TESTINGWORDSENTRY, _USER_TODAYSTUDYINGWORDSENTRY, _USER_TODAYTESTINGWORDSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=1015,
)

_TESTINGWORD.fields_by_name['last_passed_time'].message_type = _TIME
_STUDYINGWORDS.fields_by_name['studying_words'].message_type = _STUDYINGWORD
_TESTINGWORDS.fields_by_name['studying_words'].message_type = _TESTINGWORD
_USER_STUDYINGWORDSENTRY.fields_by_name['value'].message_type = _STUDYINGWORD
_USER_STUDYINGWORDSENTRY.containing_type = _USER
_USER_TESTINGWORDSENTRY.fields_by_name['value'].message_type = _TESTINGWORD
_USER_TESTINGWORDSENTRY.containing_type = _USER
_USER_TODAYSTUDYINGWORDSENTRY.fields_by_name['value'].message_type = _STUDYINGWORDS
_USER_TODAYSTUDYINGWORDSENTRY.containing_type = _USER
_USER_TODAYTESTINGWORDSENTRY.fields_by_name['value'].message_type = _TESTINGWORDS
_USER_TODAYTESTINGWORDSENTRY.containing_type = _USER
_USER.fields_by_name['last_signing_time'].message_type = _TIME
_USER.fields_by_name['studying_words'].message_type = _USER_STUDYINGWORDSENTRY
_USER.fields_by_name['testing_words'].message_type = _USER_TESTINGWORDSENTRY
_USER.fields_by_name['today_studying_words'].message_type = _USER_TODAYSTUDYINGWORDSENTRY
_USER.fields_by_name['today_testing_words'].message_type = _USER_TODAYTESTINGWORDSENTRY
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['StudyingWord'] = _STUDYINGWORD
DESCRIPTOR.message_types_by_name['TestingWord'] = _TESTINGWORD
DESCRIPTOR.message_types_by_name['StudyingWords'] = _STUDYINGWORDS
DESCRIPTOR.message_types_by_name['TestingWords'] = _TESTINGWORDS
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.Time)
  })
_sym_db.RegisterMessage(Time)

StudyingWord = _reflection.GeneratedProtocolMessageType('StudyingWord', (_message.Message,), {
  'DESCRIPTOR' : _STUDYINGWORD,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.StudyingWord)
  })
_sym_db.RegisterMessage(StudyingWord)

TestingWord = _reflection.GeneratedProtocolMessageType('TestingWord', (_message.Message,), {
  'DESCRIPTOR' : _TESTINGWORD,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.TestingWord)
  })
_sym_db.RegisterMessage(TestingWord)

StudyingWords = _reflection.GeneratedProtocolMessageType('StudyingWords', (_message.Message,), {
  'DESCRIPTOR' : _STUDYINGWORDS,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.StudyingWords)
  })
_sym_db.RegisterMessage(StudyingWords)

TestingWords = _reflection.GeneratedProtocolMessageType('TestingWords', (_message.Message,), {
  'DESCRIPTOR' : _TESTINGWORDS,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.TestingWords)
  })
_sym_db.RegisterMessage(TestingWords)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {

  'StudyingWordsEntry' : _reflection.GeneratedProtocolMessageType('StudyingWordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _USER_STUDYINGWORDSENTRY,
    '__module__' : 'user_pb2'
    # @@protoc_insertion_point(class_scope:user.User.StudyingWordsEntry)
    })
  ,

  'TestingWordsEntry' : _reflection.GeneratedProtocolMessageType('TestingWordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _USER_TESTINGWORDSENTRY,
    '__module__' : 'user_pb2'
    # @@protoc_insertion_point(class_scope:user.User.TestingWordsEntry)
    })
  ,

  'TodayStudyingWordsEntry' : _reflection.GeneratedProtocolMessageType('TodayStudyingWordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _USER_TODAYSTUDYINGWORDSENTRY,
    '__module__' : 'user_pb2'
    # @@protoc_insertion_point(class_scope:user.User.TodayStudyingWordsEntry)
    })
  ,

  'TodayTestingWordsEntry' : _reflection.GeneratedProtocolMessageType('TodayTestingWordsEntry', (_message.Message,), {
    'DESCRIPTOR' : _USER_TODAYTESTINGWORDSENTRY,
    '__module__' : 'user_pb2'
    # @@protoc_insertion_point(class_scope:user.User.TodayTestingWordsEntry)
    })
  ,
  'DESCRIPTOR' : _USER,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.User)
  })
_sym_db.RegisterMessage(User)
_sym_db.RegisterMessage(User.StudyingWordsEntry)
_sym_db.RegisterMessage(User.TestingWordsEntry)
_sym_db.RegisterMessage(User.TodayStudyingWordsEntry)
_sym_db.RegisterMessage(User.TodayTestingWordsEntry)


_USER_STUDYINGWORDSENTRY._options = None
_USER_TESTINGWORDSENTRY._options = None
_USER_TODAYSTUDYINGWORDSENTRY._options = None
_USER_TODAYTESTINGWORDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
