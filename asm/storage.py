# -*- coding: utf-8 -*-
from peewee import DatabaseProxy, Model, CharField, UUIDField, BooleanField, IntegerField, AutoField
from playhouse.db_url import connect

from .const import DATABASE_URL

database_proxy = DatabaseProxy()


class BaseModel(Model):
    '''一个基础 Model 作为全局使用，其他表均应建立其上'''
    class Meta:
        database = database_proxy


class SubjectUrl(BaseModel):
    uuid = UUIDField(index=True, primary_key=True)
    name = CharField()
    url = CharField()
    url_type = CharField()
    history_url = CharField()
    deprecation = BooleanField()


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
    latest = AutoField()


class Vmess(BaseModel):
    name = CharField()


database = connect(DATABASE_URL)
database_proxy.initialize(database)
