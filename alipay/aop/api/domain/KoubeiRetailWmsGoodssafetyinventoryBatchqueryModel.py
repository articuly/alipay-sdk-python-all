#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsGoodssafetyinventoryBatchqueryModel(object):

    def __init__(self):
        self._goods_codes = None
        self._warehouse_code = None

    @property
    def goods_codes(self):
        return self._goods_codes

    @goods_codes.setter
    def goods_codes(self, value):
        if isinstance(value, list):
            self._goods_codes = list()
            for i in value:
                self._goods_codes.append(i)
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_codes:
            if isinstance(self.goods_codes, list):
                for i in range(0, len(self.goods_codes)):
                    element = self.goods_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_codes[i] = element.to_alipay_dict()
            if hasattr(self.goods_codes, 'to_alipay_dict'):
                params['goods_codes'] = self.goods_codes.to_alipay_dict()
            else:
                params['goods_codes'] = self.goods_codes
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsGoodssafetyinventoryBatchqueryModel()
        if 'goods_codes' in d:
            o.goods_codes = d['goods_codes']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        return o


