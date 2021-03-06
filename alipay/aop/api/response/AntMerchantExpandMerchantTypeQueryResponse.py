#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandMerchantTypeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMerchantTypeQueryResponse, self).__init__()
        self._indirect_bind_type = None
        self._kb_type = None

    @property
    def indirect_bind_type(self):
        return self._indirect_bind_type

    @indirect_bind_type.setter
    def indirect_bind_type(self, value):
        self._indirect_bind_type = value
    @property
    def kb_type(self):
        return self._kb_type

    @kb_type.setter
    def kb_type(self, value):
        self._kb_type = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMerchantTypeQueryResponse, self).parse_response_content(response_content)
        if 'indirect_bind_type' in response:
            self.indirect_bind_type = response['indirect_bind_type']
        if 'kb_type' in response:
            self.kb_type = response['kb_type']
