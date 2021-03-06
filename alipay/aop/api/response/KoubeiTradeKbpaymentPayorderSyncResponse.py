#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiTradeKbpaymentPayorderSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiTradeKbpaymentPayorderSyncResponse, self).__init__()
        self._request_id = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiTradeKbpaymentPayorderSyncResponse, self).parse_response_content(response_content)
        if 'request_id' in response:
            self.request_id = response['request_id']
