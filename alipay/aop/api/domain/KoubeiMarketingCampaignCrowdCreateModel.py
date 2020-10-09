#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingCampaignCrowdCreateModel(object):

    def __init__(self):
        self._conditions = None
        self._name = None
        self._operator_id = None
        self._operator_type = None
        self._out_biz_no = None

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_type(self):
        return self._operator_type

    @operator_type.setter
    def operator_type(self, value):
        self._operator_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.conditions:
            if hasattr(self.conditions, 'to_alipay_dict'):
                params['conditions'] = self.conditions.to_alipay_dict()
            else:
                params['conditions'] = self.conditions
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_type:
            if hasattr(self.operator_type, 'to_alipay_dict'):
                params['operator_type'] = self.operator_type.to_alipay_dict()
            else:
                params['operator_type'] = self.operator_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingCampaignCrowdCreateModel()
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'name' in d:
            o.name = d['name']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_type' in d:
            o.operator_type = d['operator_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


