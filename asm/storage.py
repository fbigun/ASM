# -*- coding: utf-8 -*-
from peewee import DatabaseProxy, Model, CharField, UUIDField, BooleanField, IntegerField, DateTimeField

from playhouse.db_url import connect

from .const import DATABASE_URL

database_proxy = DatabaseProxy()


class BaseModel(Model):
    '''一个基础 Model 作为全局使用，其他表均应建立其上'''
    class Meta:     # yapf: disable
        database = database_proxy


class SubjectUrl(BaseModel):
    uuid = UUIDField(index=True, primary_key=True)
    name = CharField()
    url = CharField()
    url_type = CharField()
    history_url = CharField()
    deprecation = BooleanField()
    latest = DateTimeField()


class Ssr(BaseModel):
    name = CharField()
    groupsname = CharField()
    server = CharField()
    server_port = IntegerField()
    passwd = CharField()
    method = CharField()
    obfs = CharField()
    obfs_param = CharField()
    proto = CharField()
    proto_param = CharField()
    latest = DateTimeField()


class Vmess(BaseModel):
    name = CharField()
    version = CharField()
    server = CharField()
    server_port = CharField()
    uuid = UUIDField()
    aid = IntegerField()
    network = CharField()
    fake_type = CharField()
    host = CharField()
    path = CharField()
    tls = CharField()
    latest = DateTimeField()


database = connect(DATABASE_URL)
database_proxy.initialize(database)
