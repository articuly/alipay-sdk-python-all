#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringOrderPayCancelResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringOrderPayCancelResponse, self).__init__()
        self._action = None
        self._out_pay_no = None
        self._pay_no = None
        self._trade_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def out_pay_no(self):
        return self._out_pay_no

    @out_pay_no.setter
    def out_pay_no(self, value):
        self._out_pay_no = value
    @property
    def pay_no(self):
        return self._pay_no

    @pay_no.setter
    def pay_no(self, value):
        self._pay_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringOrderPayCancelResponse, self).parse_response_content(response_content)
        if 'action' in response:
            self.action = response['action']
        if 'out_pay_no' in response:
            self.out_pay_no = response['out_pay_no']
        if 'pay_no' in response:
            self.pay_no = response['pay_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
