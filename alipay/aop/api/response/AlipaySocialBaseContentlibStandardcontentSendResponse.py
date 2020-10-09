#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseContentlibStandardcontentSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseContentlibStandardcontentSendResponse, self).__init__()
        self._result_msg = None

    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseContentlibStandardcontentSendResponse, self).parse_response_content(response_content)
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
