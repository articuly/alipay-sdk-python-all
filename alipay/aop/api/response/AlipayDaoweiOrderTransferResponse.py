#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDaoweiOrderTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDaoweiOrderTransferResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayDaoweiOrderTransferResponse, self).parse_response_content(response_content)
