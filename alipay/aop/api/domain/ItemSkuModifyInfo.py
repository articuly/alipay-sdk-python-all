#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemExtInfo import ItemExtInfo


class ItemSkuModifyInfo(object):

    def __init__(self):
        self._cost_price = None
        self._ext_info = None
        self._original_price = None
        self._price = None
        self._sku_id = None
        self._status = None

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, value):
        self._cost_price = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ItemExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ItemExtInfo.from_alipay_dict(i))
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cost_price:
            if hasattr(self.cost_price, 'to_alipay_dict'):
                params['cost_price'] = self.cost_price.to_alipay_dict()
            else:
                params['cost_price'] = self.cost_price
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemSkuModifyInfo()
        if 'cost_price' in d:
            o.cost_price = d['cost_price']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price' in d:
            o.price = d['price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'status' in d:
            o.status = d['status']
        return o


