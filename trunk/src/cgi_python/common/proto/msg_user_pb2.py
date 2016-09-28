# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import comm_struct_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_user.proto',
  package='hoosho.user',
  serialized_pb='\n\x0emsg_user.proto\x12\x0bhoosho.user\x1a\x11\x63omm_struct.proto\"V\n\x17UpdateUserDetailInfoReq\x12;\n\x10user_detail_info\x18\x01 \x01(\x0b\x32!.hoosho.commstruct.UserDetailInfo\"\x19\n\x17UpdateUserDetailInfoRes\"1\n\x16QueryUserDetailInfoReq\x12\x17\n\x0fopenid_md5_list\x18\x01 \x03(\x04\"Z\n\x16QueryUserDetailInfoRes\x12@\n\x15user_detail_info_list\x18\x01 \x03(\x0b\x32!.hoosho.commstruct.UserDetailInfo\"&\n\x10QueryUserFansReq\x12\x12\n\nopenid_md5\x18\x01 \x01(\x04\"+\n\x10QueryUserFansRes\x12\x17\n\x0fopenid_md5_list\x18\x01 \x03(\x04\".\n\x13QueryUserFansNumReq\x12\x17\n\x0fopenid_md5_list\x18\x01 \x03(\x04\"O\n\x13QueryUserFansNumRes\x12\x38\n\rfans_num_list\x18\x01 \x03(\x0b\x32!.hoosho.commstruct.KeyValueIntInt\")\n\x13QueryUserFollowsReq\x12\x12\n\nopenid_md5\x18\x01 \x01(\x04\".\n\x13QueryUserFollowsRes\x12\x17\n\x0fopenid_md5_list\x18\x01 \x03(\x04\"Q\n\rUserFollowReq\x12\x17\n\x0fopenid_md5_from\x18\x01 \x01(\x04\x12\x15\n\ropenid_md5_to\x18\x02 \x01(\x04\x12\x10\n\x08relation\x18\x03 \x01(\x04\"\x0f\n\rUserFollowRes\"0\n\x17UserParsePreAuthCodeReq\x12\x15\n\rpre_auth_code\x18\x01 \x01(\t\"V\n\x17UserParsePreAuthCodeRes\x12;\n\x10user_detail_info\x18\x01 \x01(\x0b\x32!.hoosho.commstruct.UserDetailInfo\":\n\x11QueryUserPowerReq\x12\x12\n\nopenid_md5\x18\x01 \x01(\x04\x12\x11\n\tappid_md5\x18\x02 \x01(\x04\"\'\n\x11QueryUserPowerRes\x12\x12\n\npower_list\x18\x01 \x03(\x04\"!\n\x12QueryUserZombieReq\x12\x0b\n\x03uin\x18\x01 \x01(\t\"-\n\x12QueryUserZombieRes\x12\x17\n\x0fopenid_md5_list\x18\x01 \x03(\x04\"\x1d\n\x0eQueryUserPaReq\x12\x0b\n\x03uin\x18\x01 \x01(\t\"(\n\x0eQueryUserPaRes\x12\x16\n\x0e\x61ppid_md5_list\x18\x01 \x03(\x04\"\x17\n\x15QueryUserZomanagerReq\")\n\x15QueryUserZomanagerRes\x12\x10\n\x08uin_list\x18\x01 \x03(\t')




_UPDATEUSERDETAILINFOREQ = _descriptor.Descriptor(
  name='UpdateUserDetailInfoReq',
  full_name='hoosho.user.UpdateUserDetailInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_detail_info', full_name='hoosho.user.UpdateUserDetailInfoReq.user_detail_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=50,
  serialized_end=136,
)


_UPDATEUSERDETAILINFORES = _descriptor.Descriptor(
  name='UpdateUserDetailInfoRes',
  full_name='hoosho.user.UpdateUserDetailInfoRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=138,
  serialized_end=163,
)


_QUERYUSERDETAILINFOREQ = _descriptor.Descriptor(
  name='QueryUserDetailInfoReq',
  full_name='hoosho.user.QueryUserDetailInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_list', full_name='hoosho.user.QueryUserDetailInfoReq.openid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=165,
  serialized_end=214,
)


_QUERYUSERDETAILINFORES = _descriptor.Descriptor(
  name='QueryUserDetailInfoRes',
  full_name='hoosho.user.QueryUserDetailInfoRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_detail_info_list', full_name='hoosho.user.QueryUserDetailInfoRes.user_detail_info_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=216,
  serialized_end=306,
)


_QUERYUSERFANSREQ = _descriptor.Descriptor(
  name='QueryUserFansReq',
  full_name='hoosho.user.QueryUserFansReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5', full_name='hoosho.user.QueryUserFansReq.openid_md5', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  extension_ranges=[],
  serialized_start=308,
  serialized_end=346,
)


_QUERYUSERFANSRES = _descriptor.Descriptor(
  name='QueryUserFansRes',
  full_name='hoosho.user.QueryUserFansRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_list', full_name='hoosho.user.QueryUserFansRes.openid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=348,
  serialized_end=391,
)


_QUERYUSERFANSNUMREQ = _descriptor.Descriptor(
  name='QueryUserFansNumReq',
  full_name='hoosho.user.QueryUserFansNumReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_list', full_name='hoosho.user.QueryUserFansNumReq.openid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=393,
  serialized_end=439,
)


_QUERYUSERFANSNUMRES = _descriptor.Descriptor(
  name='QueryUserFansNumRes',
  full_name='hoosho.user.QueryUserFansNumRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fans_num_list', full_name='hoosho.user.QueryUserFansNumRes.fans_num_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=441,
  serialized_end=520,
)


_QUERYUSERFOLLOWSREQ = _descriptor.Descriptor(
  name='QueryUserFollowsReq',
  full_name='hoosho.user.QueryUserFollowsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5', full_name='hoosho.user.QueryUserFollowsReq.openid_md5', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  extension_ranges=[],
  serialized_start=522,
  serialized_end=563,
)


_QUERYUSERFOLLOWSRES = _descriptor.Descriptor(
  name='QueryUserFollowsRes',
  full_name='hoosho.user.QueryUserFollowsRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_list', full_name='hoosho.user.QueryUserFollowsRes.openid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=565,
  serialized_end=611,
)


_USERFOLLOWREQ = _descriptor.Descriptor(
  name='UserFollowReq',
  full_name='hoosho.user.UserFollowReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_from', full_name='hoosho.user.UserFollowReq.openid_md5_from', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='openid_md5_to', full_name='hoosho.user.UserFollowReq.openid_md5_to', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relation', full_name='hoosho.user.UserFollowReq.relation', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  extension_ranges=[],
  serialized_start=613,
  serialized_end=694,
)


_USERFOLLOWRES = _descriptor.Descriptor(
  name='UserFollowRes',
  full_name='hoosho.user.UserFollowRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=696,
  serialized_end=711,
)


_USERPARSEPREAUTHCODEREQ = _descriptor.Descriptor(
  name='UserParsePreAuthCodeReq',
  full_name='hoosho.user.UserParsePreAuthCodeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pre_auth_code', full_name='hoosho.user.UserParsePreAuthCodeReq.pre_auth_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=713,
  serialized_end=761,
)


_USERPARSEPREAUTHCODERES = _descriptor.Descriptor(
  name='UserParsePreAuthCodeRes',
  full_name='hoosho.user.UserParsePreAuthCodeRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_detail_info', full_name='hoosho.user.UserParsePreAuthCodeRes.user_detail_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=763,
  serialized_end=849,
)


_QUERYUSERPOWERREQ = _descriptor.Descriptor(
  name='QueryUserPowerReq',
  full_name='hoosho.user.QueryUserPowerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5', full_name='hoosho.user.QueryUserPowerReq.openid_md5', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appid_md5', full_name='hoosho.user.QueryUserPowerReq.appid_md5', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  extension_ranges=[],
  serialized_start=851,
  serialized_end=909,
)


_QUERYUSERPOWERRES = _descriptor.Descriptor(
  name='QueryUserPowerRes',
  full_name='hoosho.user.QueryUserPowerRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='power_list', full_name='hoosho.user.QueryUserPowerRes.power_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=911,
  serialized_end=950,
)


_QUERYUSERZOMBIEREQ = _descriptor.Descriptor(
  name='QueryUserZombieReq',
  full_name='hoosho.user.QueryUserZombieReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin', full_name='hoosho.user.QueryUserZombieReq.uin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=952,
  serialized_end=985,
)


_QUERYUSERZOMBIERES = _descriptor.Descriptor(
  name='QueryUserZombieRes',
  full_name='hoosho.user.QueryUserZombieRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='openid_md5_list', full_name='hoosho.user.QueryUserZombieRes.openid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=987,
  serialized_end=1032,
)


_QUERYUSERPAREQ = _descriptor.Descriptor(
  name='QueryUserPaReq',
  full_name='hoosho.user.QueryUserPaReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin', full_name='hoosho.user.QueryUserPaReq.uin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=1034,
  serialized_end=1063,
)


_QUERYUSERPARES = _descriptor.Descriptor(
  name='QueryUserPaRes',
  full_name='hoosho.user.QueryUserPaRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid_md5_list', full_name='hoosho.user.QueryUserPaRes.appid_md5_list', index=0,
      number=1, type=4, cpp_type=4, label=3,
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
  extension_ranges=[],
  serialized_start=1065,
  serialized_end=1105,
)


_QUERYUSERZOMANAGERREQ = _descriptor.Descriptor(
  name='QueryUserZomanagerReq',
  full_name='hoosho.user.QueryUserZomanagerReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1107,
  serialized_end=1130,
)


_QUERYUSERZOMANAGERRES = _descriptor.Descriptor(
  name='QueryUserZomanagerRes',
  full_name='hoosho.user.QueryUserZomanagerRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uin_list', full_name='hoosho.user.QueryUserZomanagerRes.uin_list', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=1132,
  serialized_end=1173,
)

_UPDATEUSERDETAILINFOREQ.fields_by_name['user_detail_info'].message_type = comm_struct_pb2._USERDETAILINFO
_QUERYUSERDETAILINFORES.fields_by_name['user_detail_info_list'].message_type = comm_struct_pb2._USERDETAILINFO
_QUERYUSERFANSNUMRES.fields_by_name['fans_num_list'].message_type = comm_struct_pb2._KEYVALUEINTINT
_USERPARSEPREAUTHCODERES.fields_by_name['user_detail_info'].message_type = comm_struct_pb2._USERDETAILINFO
DESCRIPTOR.message_types_by_name['UpdateUserDetailInfoReq'] = _UPDATEUSERDETAILINFOREQ
DESCRIPTOR.message_types_by_name['UpdateUserDetailInfoRes'] = _UPDATEUSERDETAILINFORES
DESCRIPTOR.message_types_by_name['QueryUserDetailInfoReq'] = _QUERYUSERDETAILINFOREQ
DESCRIPTOR.message_types_by_name['QueryUserDetailInfoRes'] = _QUERYUSERDETAILINFORES
DESCRIPTOR.message_types_by_name['QueryUserFansReq'] = _QUERYUSERFANSREQ
DESCRIPTOR.message_types_by_name['QueryUserFansRes'] = _QUERYUSERFANSRES
DESCRIPTOR.message_types_by_name['QueryUserFansNumReq'] = _QUERYUSERFANSNUMREQ
DESCRIPTOR.message_types_by_name['QueryUserFansNumRes'] = _QUERYUSERFANSNUMRES
DESCRIPTOR.message_types_by_name['QueryUserFollowsReq'] = _QUERYUSERFOLLOWSREQ
DESCRIPTOR.message_types_by_name['QueryUserFollowsRes'] = _QUERYUSERFOLLOWSRES
DESCRIPTOR.message_types_by_name['UserFollowReq'] = _USERFOLLOWREQ
DESCRIPTOR.message_types_by_name['UserFollowRes'] = _USERFOLLOWRES
DESCRIPTOR.message_types_by_name['UserParsePreAuthCodeReq'] = _USERPARSEPREAUTHCODEREQ
DESCRIPTOR.message_types_by_name['UserParsePreAuthCodeRes'] = _USERPARSEPREAUTHCODERES
DESCRIPTOR.message_types_by_name['QueryUserPowerReq'] = _QUERYUSERPOWERREQ
DESCRIPTOR.message_types_by_name['QueryUserPowerRes'] = _QUERYUSERPOWERRES
DESCRIPTOR.message_types_by_name['QueryUserZombieReq'] = _QUERYUSERZOMBIEREQ
DESCRIPTOR.message_types_by_name['QueryUserZombieRes'] = _QUERYUSERZOMBIERES
DESCRIPTOR.message_types_by_name['QueryUserPaReq'] = _QUERYUSERPAREQ
DESCRIPTOR.message_types_by_name['QueryUserPaRes'] = _QUERYUSERPARES
DESCRIPTOR.message_types_by_name['QueryUserZomanagerReq'] = _QUERYUSERZOMANAGERREQ
DESCRIPTOR.message_types_by_name['QueryUserZomanagerRes'] = _QUERYUSERZOMANAGERRES

class UpdateUserDetailInfoReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEUSERDETAILINFOREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.UpdateUserDetailInfoReq)

class UpdateUserDetailInfoRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEUSERDETAILINFORES

  # @@protoc_insertion_point(class_scope:hoosho.user.UpdateUserDetailInfoRes)

class QueryUserDetailInfoReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERDETAILINFOREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserDetailInfoReq)

class QueryUserDetailInfoRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERDETAILINFORES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserDetailInfoRes)

class QueryUserFansReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFANSREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFansReq)

class QueryUserFansRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFANSRES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFansRes)

class QueryUserFansNumReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFANSNUMREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFansNumReq)

class QueryUserFansNumRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFANSNUMRES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFansNumRes)

class QueryUserFollowsReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFOLLOWSREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFollowsReq)

class QueryUserFollowsRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERFOLLOWSRES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserFollowsRes)

class UserFollowReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERFOLLOWREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.UserFollowReq)

class UserFollowRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERFOLLOWRES

  # @@protoc_insertion_point(class_scope:hoosho.user.UserFollowRes)

class UserParsePreAuthCodeReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERPARSEPREAUTHCODEREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.UserParsePreAuthCodeReq)

class UserParsePreAuthCodeRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USERPARSEPREAUTHCODERES

  # @@protoc_insertion_point(class_scope:hoosho.user.UserParsePreAuthCodeRes)

class QueryUserPowerReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERPOWERREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserPowerReq)

class QueryUserPowerRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERPOWERRES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserPowerRes)

class QueryUserZombieReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERZOMBIEREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserZombieReq)

class QueryUserZombieRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERZOMBIERES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserZombieRes)

class QueryUserPaReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERPAREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserPaReq)

class QueryUserPaRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERPARES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserPaRes)

class QueryUserZomanagerReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERZOMANAGERREQ

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserZomanagerReq)

class QueryUserZomanagerRes(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYUSERZOMANAGERRES

  # @@protoc_insertion_point(class_scope:hoosho.user.QueryUserZomanagerRes)


# @@protoc_insertion_point(module_scope)