#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenNewgotoneCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenNewgotoneCreateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenNewgotoneCreateResponse, self).parse_response_content(response_content)
