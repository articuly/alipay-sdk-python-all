#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingExitinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingExitinfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingExitinfoSyncResponse, self).parse_response_content(response_content)
