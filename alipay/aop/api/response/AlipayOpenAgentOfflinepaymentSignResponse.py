#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentOfflinepaymentSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentOfflinepaymentSignResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentOfflinepaymentSignResponse, self).parse_response_content(response_content)
