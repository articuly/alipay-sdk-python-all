#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class MybankFinanceYulibaoPriceQueryModel(object):

    def __init__(self):
        self._end_date = None
        self._fund_code = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.fund_code:
            if hasattr(self.fund_code, 'to_alipay_dict'):
                params['fund_code'] = self.fund_code.to_alipay_dict()
            else:
                params['fund_code'] = self.fund_code
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankFinanceYulibaoPriceQueryModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'fund_code' in d:
            o.fund_code = d['fund_code']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


