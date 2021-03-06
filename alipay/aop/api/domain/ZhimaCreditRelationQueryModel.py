#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditRelationQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._linked_merchant_id = None
        self._name = None
        self._product_code = None
        self._relation = None
        self._relation_name = None
        self._relation_phone = None
        self._transaction_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def linked_merchant_id(self):
        return self._linked_merchant_id

    @linked_merchant_id.setter
    def linked_merchant_id(self, value):
        self._linked_merchant_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def relation(self):
        return self._relation

    @relation.setter
    def relation(self, value):
        self._relation = value
    @property
    def relation_name(self):
        return self._relation_name

    @relation_name.setter
    def relation_name(self, value):
        self._relation_name = value
    @property
    def relation_phone(self):
        return self._relation_phone

    @relation_phone.setter
    def relation_phone(self, value):
        self._relation_phone = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.linked_merchant_id:
            if hasattr(self.linked_merchant_id, 'to_alipay_dict'):
                params['linked_merchant_id'] = self.linked_merchant_id.to_alipay_dict()
            else:
                params['linked_merchant_id'] = self.linked_merchant_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.relation:
            if hasattr(self.relation, 'to_alipay_dict'):
                params['relation'] = self.relation.to_alipay_dict()
            else:
                params['relation'] = self.relation
        if self.relation_name:
            if hasattr(self.relation_name, 'to_alipay_dict'):
                params['relation_name'] = self.relation_name.to_alipay_dict()
            else:
                params['relation_name'] = self.relation_name
        if self.relation_phone:
            if hasattr(self.relation_phone, 'to_alipay_dict'):
                params['relation_phone'] = self.relation_phone.to_alipay_dict()
            else:
                params['relation_phone'] = self.relation_phone
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditRelationQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'linked_merchant_id' in d:
            o.linked_merchant_id = d['linked_merchant_id']
        if 'name' in d:
            o.name = d['name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'relation' in d:
            o.relation = d['relation']
        if 'relation_name' in d:
            o.relation_name = d['relation_name']
        if 'relation_phone' in d:
            o.relation_phone = d['relation_phone']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        return o


