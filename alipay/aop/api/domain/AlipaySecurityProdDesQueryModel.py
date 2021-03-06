#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavinTestnew import GavinTestnew


class AlipaySecurityProdDesQueryModel(object):

    def __init__(self):
        self._com = None
        self._test = None

    @property
    def com(self):
        return self._com

    @com.setter
    def com(self, value):
        if isinstance(value, GavinTestnew):
            self._com = value
        else:
            self._com = GavinTestnew.from_alipay_dict(value)
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, list):
            self._test = list()
            for i in value:
                self._test.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.com:
            if hasattr(self.com, 'to_alipay_dict'):
                params['com'] = self.com.to_alipay_dict()
            else:
                params['com'] = self.com
        if self.test:
            if isinstance(self.test, list):
                for i in range(0, len(self.test)):
                    element = self.test[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test[i] = element.to_alipay_dict()
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdDesQueryModel()
        if 'com' in d:
            o.com = d['com']
        if 'test' in d:
            o.test = d['test']
        return o


