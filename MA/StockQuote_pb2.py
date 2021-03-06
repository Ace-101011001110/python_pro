# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: StockQuote.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='StockQuote.proto',
  package='protobuf',
  syntax='proto2',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10StockQuote.proto\x12\x08protobuf\"\xf9\x08\n\nStockQuote\x12\x0b\n\x03sym\x18\x01 \x01(\t\x12\x12\n\x07\x62id_pri\x18\x02 \x01(\x01:\x01\x30\x12\x11\n\x06\x62id_sz\x18\x03 \x01(\x11:\x01\x30\x12\x12\n\x07\x61sk_pri\x18\x04 \x01(\x01:\x01\x30\x12\x11\n\x06\x61sk_sz\x18\x05 \x01(\x11:\x01\x30\x12\x13\n\x08last_pri\x18\x06 \x01(\x01:\x01\x30\x12\x12\n\x07last_sz\x18\x07 \x01(\x11:\x01\x30\x12\x14\n\ttottrd_sz\x18\x08 \x01(\x01:\x01\x30\x12\x16\n\x0blast_bid_tm\x18\t \x01(\x11:\x01\x30\x12\x16\n\x0blast_ask_tm\x18\n \x01(\x11:\x01\x30\x12\x16\n\x0blast_trd_tm\x18\x0b \x01(\x11:\x01\x30\x12\x15\n\npreclo_pri\x18\x0c \x01(\x01:\x01\x30\x12\x12\n\x07opn_pri\x18\r \x01(\x01:\x01\x30\x12\x13\n\x08high_pri\x18\x0e \x01(\x01:\x01\x30\x12\x12\n\x07low_pri\x18\x0f \x01(\x01:\x01\x30\x12\x16\n\x0b\x62id_aggr_sz\x18\x10 \x01(\x11:\x01\x30\x12\x16\n\x0b\x61sk_aggr_sz\x18\x11 \x01(\x11:\x01\x30\x12\x14\n\tbid_count\x18\x12 \x01(\x11:\x01\x30\x12\x14\n\task_count\x18\x13 \x01(\x11:\x01\x30\x12\x16\n\x0blast_trd_dt\x18\x14 \x01(\x11:\x01\x30\x12\x16\n\x0blast_bid_dt\x18\x15 \x01(\x11:\x01\x30\x12\x16\n\x0blast_ask_dt\x18\x16 \x01(\x11:\x01\x30\x12\x0f\n\x04vwap\x18\x17 \x01(\x01:\x01\x30\x12\x13\n\x08vwap_vol\x18\x18 \x01(\x11:\x01\x30\x12\x15\n\nquote_cond\x18\x19 \x01(\x07:\x01\x30\x12\x15\n\ntrade_cond\x18\x1a \x01(\x07:\x01\x30\x12\x1a\n\x0fsequence_number\x18\x1b \x01(\x12:\x01\x30\x12\x0f\n\x04\x65xch\x18\x1c \x01(\x11:\x01\x30\x12\x1a\n\x0c\x64\x65\x63ision_tag\x18\x1d \x01(\x08:\x04true\x12\x13\n\x08\x62id_mmid\x18\x1e \x01(\x07:\x01\x30\x12\x13\n\x08\x61sk_mmid\x18\x1f \x01(\x07:\x01\x30\x12\x18\n\rtrade_exch_id\x18  \x01(\x07:\x01\x30\x12\x16\n\x0bpre_clo_spl\x18! \x01(\x01:\x01\x30\x12\x15\n\ntottrd_amt\x18\" \x01(\x01:\x01\x30\x12\x15\n\x06\x61\x64vise\x18# \x01(\x08:\x05\x66\x61lse\x12\x15\n\x08\x62id_tick\x18$ \x01(\x05:\x03\x31\x31\x31\x12\x15\n\x08\x61sk_tick\x18% \x01(\x05:\x03\x31\x31\x31\x12\x11\n\x06status\x18& \x01(\x11:\x01\x30\x12\x11\n\x06no_qts\x18\' \x01(\x05:\x01\x30\x12\x12\n\x07no_trds\x18( \x01(\x05:\x01\x30\x12\x17\n\x0clast_recv_tm\x18) \x01(\x11:\x01\x30\x12\x1d\n\x12sampling_timestamp\x18* \x01(\x12:\x01\x30\x12\x16\n\x0brecv_utc_dt\x18+ \x01(\x11:\x01\x30\x12\x16\n\x0brecv_utc_tm\x18, \x01(\x11:\x01\x30\x12\x1a\n\x0flast_bid_utc_ts\x18- \x01(\x12:\x01\x30\x12\x1a\n\x0flast_ask_utc_ts\x18. \x01(\x12:\x01\x30\x12\x1a\n\x0flast_trd_utc_ts\x18/ \x01(\x12:\x01\x30\x12\x18\n\ropen_interest\x18\x30 \x01(\x01:\x01\x30\x12\x15\n\nsrc_utc_ts\x18\x31 \x01(\x12:\x01\x30\x12\x15\n\nsnk_utc_ts\x18\x32 \x01(\x12:\x01\x30\x42\x02H\x03'
)




_STOCKQUOTE = _descriptor.Descriptor(
  name='StockQuote',
  full_name='protobuf.StockQuote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sym', full_name='protobuf.StockQuote.sym', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_pri', full_name='protobuf.StockQuote.bid_pri', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_sz', full_name='protobuf.StockQuote.bid_sz', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_pri', full_name='protobuf.StockQuote.ask_pri', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_sz', full_name='protobuf.StockQuote.ask_sz', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_pri', full_name='protobuf.StockQuote.last_pri', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_sz', full_name='protobuf.StockQuote.last_sz', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tottrd_sz', full_name='protobuf.StockQuote.tottrd_sz', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_bid_tm', full_name='protobuf.StockQuote.last_bid_tm', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_ask_tm', full_name='protobuf.StockQuote.last_ask_tm', index=9,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_trd_tm', full_name='protobuf.StockQuote.last_trd_tm', index=10,
      number=11, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preclo_pri', full_name='protobuf.StockQuote.preclo_pri', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opn_pri', full_name='protobuf.StockQuote.opn_pri', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_pri', full_name='protobuf.StockQuote.high_pri', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low_pri', full_name='protobuf.StockQuote.low_pri', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_aggr_sz', full_name='protobuf.StockQuote.bid_aggr_sz', index=15,
      number=16, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_aggr_sz', full_name='protobuf.StockQuote.ask_aggr_sz', index=16,
      number=17, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_count', full_name='protobuf.StockQuote.bid_count', index=17,
      number=18, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_count', full_name='protobuf.StockQuote.ask_count', index=18,
      number=19, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_trd_dt', full_name='protobuf.StockQuote.last_trd_dt', index=19,
      number=20, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_bid_dt', full_name='protobuf.StockQuote.last_bid_dt', index=20,
      number=21, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_ask_dt', full_name='protobuf.StockQuote.last_ask_dt', index=21,
      number=22, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vwap', full_name='protobuf.StockQuote.vwap', index=22,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vwap_vol', full_name='protobuf.StockQuote.vwap_vol', index=23,
      number=24, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote_cond', full_name='protobuf.StockQuote.quote_cond', index=24,
      number=25, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trade_cond', full_name='protobuf.StockQuote.trade_cond', index=25,
      number=26, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='protobuf.StockQuote.sequence_number', index=26,
      number=27, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exch', full_name='protobuf.StockQuote.exch', index=27,
      number=28, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decision_tag', full_name='protobuf.StockQuote.decision_tag', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_mmid', full_name='protobuf.StockQuote.bid_mmid', index=29,
      number=30, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_mmid', full_name='protobuf.StockQuote.ask_mmid', index=30,
      number=31, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trade_exch_id', full_name='protobuf.StockQuote.trade_exch_id', index=31,
      number=32, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pre_clo_spl', full_name='protobuf.StockQuote.pre_clo_spl', index=32,
      number=33, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tottrd_amt', full_name='protobuf.StockQuote.tottrd_amt', index=33,
      number=34, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advise', full_name='protobuf.StockQuote.advise', index=34,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bid_tick', full_name='protobuf.StockQuote.bid_tick', index=35,
      number=36, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=111,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ask_tick', full_name='protobuf.StockQuote.ask_tick', index=36,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=111,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='protobuf.StockQuote.status', index=37,
      number=38, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='no_qts', full_name='protobuf.StockQuote.no_qts', index=38,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='no_trds', full_name='protobuf.StockQuote.no_trds', index=39,
      number=40, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_recv_tm', full_name='protobuf.StockQuote.last_recv_tm', index=40,
      number=41, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sampling_timestamp', full_name='protobuf.StockQuote.sampling_timestamp', index=41,
      number=42, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recv_utc_dt', full_name='protobuf.StockQuote.recv_utc_dt', index=42,
      number=43, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recv_utc_tm', full_name='protobuf.StockQuote.recv_utc_tm', index=43,
      number=44, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_bid_utc_ts', full_name='protobuf.StockQuote.last_bid_utc_ts', index=44,
      number=45, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_ask_utc_ts', full_name='protobuf.StockQuote.last_ask_utc_ts', index=45,
      number=46, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_trd_utc_ts', full_name='protobuf.StockQuote.last_trd_utc_ts', index=46,
      number=47, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open_interest', full_name='protobuf.StockQuote.open_interest', index=47,
      number=48, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='src_utc_ts', full_name='protobuf.StockQuote.src_utc_ts', index=48,
      number=49, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snk_utc_ts', full_name='protobuf.StockQuote.snk_utc_ts', index=49,
      number=50, type=18, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=1176,
)

DESCRIPTOR.message_types_by_name['StockQuote'] = _STOCKQUOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StockQuote = _reflection.GeneratedProtocolMessageType('StockQuote', (_message.Message,), {
  'DESCRIPTOR' : _STOCKQUOTE,
  '__module__' : 'StockQuote_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.StockQuote)
  })
_sym_db.RegisterMessage(StockQuote)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
