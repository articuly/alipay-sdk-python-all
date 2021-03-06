#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayAcquirePrecreateRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._body = None
        self._channel_parameters = None
        self._currency = None
        self._extend_params = None
        self._goods_detail = None
        self._it_b_pay = None
        self._operator_code = None
        self._operator_id = None
        self._out_trade_no = None
        self._price = None
        self._quantity = None
        self._royalty_parameters = None
        self._royalty_type = None
        self._seller_email = None
        self._seller_id = None
        self._show_url = None
        self._subject = None
        self._total_fee = None
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
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def channel_parameters(self):
        return self._channel_parameters

    @channel_parameters.setter
    def channel_parameters(self, value):
        self._channel_parameters = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def goods_detail(self):
        return self._goods_detail

    @goods_detail.setter
    def goods_detail(self, value):
        self._goods_detail = value
    @property
    def it_b_pay(self):
        return self._it_b_pay

    @it_b_pay.setter
    def it_b_pay(self, value):
        self._it_b_pay = value
    @property
    def operator_code(self):
        return self._operator_code

    @operator_code.setter
    def operator_code(self, value):
        self._operator_code = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def royalty_parameters(self):
        return self._royalty_parameters

    @royalty_parameters.setter
    def royalty_parameters(self, value):
        self._royalty_parameters = value
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value
    @property
    def seller_email(self):
        return self._seller_email

    @seller_email.setter
    def seller_email(self, value):
        self._seller_email = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def show_url(self):
        return self._show_url

    @show_url.setter
    def show_url(self, value):
        self._show_url = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_fee(self):
        return self._total_fee

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value


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
        params[P_METHOD] = 'alipay.acquire.precreate'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = json.dumps(obj=self.body.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['body'] = self.body
        if self.channel_parameters:
            if hasattr(self.channel_parameters, 'to_alipay_dict'):
                params['channel_parameters'] = json.dumps(obj=self.channel_parameters.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['channel_parameters'] = self.channel_parameters
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = json.dumps(obj=self.currency.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['currency'] = self.currency
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = json.dumps(obj=self.extend_params.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['extend_params'] = self.extend_params
        if self.goods_detail:
            if hasattr(self.goods_detail, 'to_alipay_dict'):
                params['goods_detail'] = json.dumps(obj=self.goods_detail.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['goods_detail'] = self.goods_detail
        if self.it_b_pay:
            if hasattr(self.it_b_pay, 'to_alipay_dict'):
                params['it_b_pay'] = json.dumps(obj=self.it_b_pay.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['it_b_pay'] = self.it_b_pay
        if self.operator_code:
            if hasattr(self.operator_code, 'to_alipay_dict'):
                params['operator_code'] = json.dumps(obj=self.operator_code.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['operator_code'] = self.operator_code
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = json.dumps(obj=self.operator_id.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['operator_id'] = self.operator_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = json.dumps(obj=self.out_trade_no.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = json.dumps(obj=self.price.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = json.dumps(obj=self.quantity.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['quantity'] = self.quantity
        if self.royalty_parameters:
            if hasattr(self.royalty_parameters, 'to_alipay_dict'):
                params['royalty_parameters'] = json.dumps(obj=self.royalty_parameters.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['royalty_parameters'] = self.royalty_parameters
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = json.dumps(obj=self.royalty_type.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['royalty_type'] = self.royalty_type
        if self.seller_email:
            if hasattr(self.seller_email, 'to_alipay_dict'):
                params['seller_email'] = json.dumps(obj=self.seller_email.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_email'] = self.seller_email
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = json.dumps(obj=self.seller_id.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['seller_id'] = self.seller_id
        if self.show_url:
            if hasattr(self.show_url, 'to_alipay_dict'):
                params['show_url'] = json.dumps(obj=self.show_url.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['show_url'] = self.show_url
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = json.dumps(obj=self.subject.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['subject'] = self.subject
        if self.total_fee:
            if hasattr(self.total_fee, 'to_alipay_dict'):
                params['total_fee'] = json.dumps(obj=self.total_fee.to_alipay_dict(), use_decimal=True, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['total_fee'] = self.total_fee
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
