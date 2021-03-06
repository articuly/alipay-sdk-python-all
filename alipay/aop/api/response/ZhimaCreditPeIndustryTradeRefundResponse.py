#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeIndustryTradeRefundResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeIndustryTradeRefundResponse, self).__init__()
        self._alipay_fund_order_no = None
        self._alipay_out_trade_no = None
        self._amount = None
        self._message = None
        self._out_fund_no = None
        self._out_refund_no = None
        self._pay_time = None
        self._refund_status = None
        self._zm_order_id = None

    @property
    def alipay_fund_order_no(self):
        return self._alipay_fund_order_no

    @alipay_fund_order_no.setter
    def alipay_fund_order_no(self, value):
        self._alipay_fund_order_no = value
    @property
    def alipay_out_trade_no(self):
        return self._alipay_out_trade_no

    @alipay_out_trade_no.setter
    def alipay_out_trade_no(self, value):
        self._alipay_out_trade_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def out_fund_no(self):
        return self._out_fund_no

    @out_fund_no.setter
    def out_fund_no(self, value):
        self._out_fund_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def zm_order_id(self):
        return self._zm_order_id

    @zm_order_id.setter
    def zm_order_id(self, value):
        self._zm_order_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeIndustryTradeRefundResponse, self).parse_response_content(response_content)
        if 'alipay_fund_order_no' in response:
            self.alipay_fund_order_no = response['alipay_fund_order_no']
        if 'alipay_out_trade_no' in response:
            self.alipay_out_trade_no = response['alipay_out_trade_no']
        if 'amount' in response:
            self.amount = response['amount']
        if 'message' in response:
            self.message = response['message']
        if 'out_fund_no' in response:
            self.out_fund_no = response['out_fund_no']
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'zm_order_id' in response:
            self.zm_order_id = response['zm_order_id']
