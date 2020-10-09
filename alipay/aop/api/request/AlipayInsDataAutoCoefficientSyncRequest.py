#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayInsDataAutoCoefficientSyncRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._coeffecient_table_id = None
        self._coeffecient_table_size = None
        self._request_id = None
        self._coeffecient_table_content = None
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
    def coeffecient_table_id(self):
        return self._coeffecient_table_id

    @coeffecient_table_id.setter
    def coeffecient_table_id(self, value):
        self._coeffecient_table_id = value
    @property
    def coeffecient_table_size(self):
        return self._coeffecient_table_size

    @coeffecient_table_size.setter
    def coeffecient_table_size(self, value):
        self._coeffecient_table_size = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    @property
    def coeffecient_table_content(self):
        return self._coeffecient_table_content

    @coeffecient_table_content.setter
    def coeffecient_table_content(self, value):
        if not isinstance(value, FileItem):
            return
        self._coeffecient_table_content = value

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
        params[P_METHOD] = 'alipay.ins.data.auto.coefficient.sync'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.coeffecient_table_id:
            if hasattr(self.coeffecient_table_id, 'to_alipay_dict'):
                params['coeffecient_table_id'] = json.dumps(obj=self.coeffecient_table_id.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['coeffecient_table_id'] = self.coeffecient_table_id
        if self.coeffecient_table_size:
            if hasattr(self.coeffecient_table_size, 'to_alipay_dict'):
                params['coeffecient_table_size'] = json.dumps(obj=self.coeffecient_table_size.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['coeffecient_table_size'] = self.coeffecient_table_size
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = json.dumps(obj=self.request_id.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['request_id'] = self.request_id
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
        if self.coeffecient_table_content:
            multipart_params['coeffecient_table_content'] = self.coeffecient_table_content
        return multipart_params
