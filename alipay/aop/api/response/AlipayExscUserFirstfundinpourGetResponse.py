#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayExscUserFirstfundinpourGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayExscUserFirstfundinpourGetResponse, self).__init__()
        self._biz_type = None
        self._success = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayExscUserFirstfundinpourGetResponse, self).parse_response_content(response_content)
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'success' in response:
            self.success = response['success']
