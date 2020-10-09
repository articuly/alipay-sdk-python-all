#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayZdataserviceUnidataQueryRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._query_condition = None
        self._uniq_key = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def query_condition(self):
        return self._query_condition

    @query_condition.setter
    def query_condition(self, value):
        self._query_condition = value
    @property
    def uniq_key(self):
        return self._uniq_key

    @uniq_key.setter
    def uniq_key(self, value):
        self._uniq_key = value


    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.zdataservice.unidata.query'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.query_condition:
            if hasattr(self.query_condition, 'to_alipay_dict'):
                params['query_condition'] = json.dumps(obj=self.query_condition.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['query_condition'] = self.query_condition
        if self.uniq_key:
            if hasattr(self.uniq_key, 'to_alipay_dict'):
                params['uniq_key'] = json.dumps(obj=self.uniq_key.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['uniq_key'] = self.uniq_key
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        return multipart_params
