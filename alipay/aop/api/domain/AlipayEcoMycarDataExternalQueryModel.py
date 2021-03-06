#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDataExternalQueryModel(object):

    def __init__(self):
        self._external_system_name = None
        self._is_transfer_uid = None
        self._operate_type = None
        self._query_condition = None

    @property
    def external_system_name(self):
        return self._external_system_name

    @external_system_name.setter
    def external_system_name(self, value):
        self._external_system_name = value
    @property
    def is_transfer_uid(self):
        return self._is_transfer_uid

    @is_transfer_uid.setter
    def is_transfer_uid(self, value):
        self._is_transfer_uid = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def query_condition(self):
        return self._query_condition

    @query_condition.setter
    def query_condition(self, value):
        self._query_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_system_name:
            if hasattr(self.external_system_name, 'to_alipay_dict'):
                params['external_system_name'] = self.external_system_name.to_alipay_dict()
            else:
                params['external_system_name'] = self.external_system_name
        if self.is_transfer_uid:
            if hasattr(self.is_transfer_uid, 'to_alipay_dict'):
                params['is_transfer_uid'] = self.is_transfer_uid.to_alipay_dict()
            else:
                params['is_transfer_uid'] = self.is_transfer_uid
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.query_condition:
            if hasattr(self.query_condition, 'to_alipay_dict'):
                params['query_condition'] = self.query_condition.to_alipay_dict()
            else:
                params['query_condition'] = self.query_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDataExternalQueryModel()
        if 'external_system_name' in d:
            o.external_system_name = d['external_system_name']
        if 'is_transfer_uid' in d:
            o.is_transfer_uid = d['is_transfer_uid']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'query_condition' in d:
            o.query_condition = d['query_condition']
        return o


