#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayCodeRecoResult import AlipayCodeRecoResult


class AlipayDataDataserviceCodeRecoResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceCodeRecoResponse, self).__init__()
        self._result = None

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, AlipayCodeRecoResult):
            self._result = value
        else:
            self._result = AlipayCodeRecoResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceCodeRecoResponse, self).parse_response_content(response_content)
        if 'result' in response:
            self.result = response['result']
