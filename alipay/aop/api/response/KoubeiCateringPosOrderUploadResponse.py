#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosOrderUploadResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosOrderUploadResponse, self).__init__()
        self._flow_id = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosOrderUploadResponse, self).parse_response_content(response_content)
        if 'flow_id' in response:
            self.flow_id = response['flow_id']
