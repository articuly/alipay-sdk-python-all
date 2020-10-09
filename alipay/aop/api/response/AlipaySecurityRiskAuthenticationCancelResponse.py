#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskAuthenticationCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskAuthenticationCancelResponse, self).__init__()
        self._biz_result = None

    @property
    def biz_result(self):
        return self._biz_result

    @biz_result.setter
    def biz_result(self, value):
        self._biz_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskAuthenticationCancelResponse, self).parse_response_content(response_content)
        if 'biz_result' in response:
            self.biz_result = response['biz_result']
