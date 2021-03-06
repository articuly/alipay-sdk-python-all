#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMessageTopicSubscribeModel(object):

    def __init__(self):
        self._auth_token = None
        self._auth_type = None
        self._comm_type = None
        self._topic = None

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def comm_type(self):
        return self._comm_type

    @comm_type.setter
    def comm_type(self, value):
        self._comm_type = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_token:
            if hasattr(self.auth_token, 'to_alipay_dict'):
                params['auth_token'] = self.auth_token.to_alipay_dict()
            else:
                params['auth_token'] = self.auth_token
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.comm_type:
            if hasattr(self.comm_type, 'to_alipay_dict'):
                params['comm_type'] = self.comm_type.to_alipay_dict()
            else:
                params['comm_type'] = self.comm_type
        if self.topic:
            if hasattr(self.topic, 'to_alipay_dict'):
                params['topic'] = self.topic.to_alipay_dict()
            else:
                params['topic'] = self.topic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMessageTopicSubscribeModel()
        if 'auth_token' in d:
            o.auth_token = d['auth_token']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'comm_type' in d:
            o.comm_type = d['comm_type']
        if 'topic' in d:
            o.topic = d['topic']
        return o


