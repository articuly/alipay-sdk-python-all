#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodRefundResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodRefundResponse, self).parse_response_content(response_content)
