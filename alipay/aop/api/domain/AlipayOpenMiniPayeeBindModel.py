#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniPayeeBindModel(object):

    def __init__(self):
        self._logonid = None
        self._pid = None

    @property
    def logonid(self):
        return self._logonid

    @logonid.setter
    def logonid(self, value):
        self._logonid = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.logonid:
            if hasattr(self.logonid, 'to_alipay_dict'):
                params['logonid'] = self.logonid.to_alipay_dict()
            else:
                params['logonid'] = self.logonid
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniPayeeBindModel()
        if 'logonid' in d:
            o.logonid = d['logonid']
        if 'pid' in d:
            o.pid = d['pid']
        return o


