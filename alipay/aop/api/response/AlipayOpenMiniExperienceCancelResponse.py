#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniExperienceCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniExperienceCancelResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniExperienceCancelResponse, self).parse_response_content(response_content)
