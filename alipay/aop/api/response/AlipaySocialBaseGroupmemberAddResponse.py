#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseGroupmemberAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseGroupmemberAddResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseGroupmemberAddResponse, self).parse_response_content(response_content)
