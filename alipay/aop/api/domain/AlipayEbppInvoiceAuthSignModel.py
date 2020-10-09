#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceAuthSignModel(object):

    def __init__(self):
        self._authorization_type = None
        self._m_short_name = None
        self._user_id = None

    @property
    def authorization_type(self):
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, value):
        self._authorization_type = value
    @property
    def m_short_name(self):
        return self._m_short_name

    @m_short_name.setter
    def m_short_name(self, value):
        self._m_short_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_type:
            if hasattr(self.authorization_type, 'to_alipay_dict'):
                params['authorization_type'] = self.authorization_type.to_alipay_dict()
            else:
                params['authorization_type'] = self.authorization_type
        if self.m_short_name:
            if hasattr(self.m_short_name, 'to_alipay_dict'):
                params['m_short_name'] = self.m_short_name.to_alipay_dict()
            else:
                params['m_short_name'] = self.m_short_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceAuthSignModel()
        if 'authorization_type' in d:
            o.authorization_type = d['authorization_type']
        if 'm_short_name' in d:
            o.m_short_name = d['m_short_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


