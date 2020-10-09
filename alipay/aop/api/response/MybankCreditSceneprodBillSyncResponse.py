#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditSceneprodBillSyncResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSceneprodBillSyncResponse, self).__init__()
        self._trace_id = None

    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSceneprodBillSyncResponse, self).parse_response_content(response_content)
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
