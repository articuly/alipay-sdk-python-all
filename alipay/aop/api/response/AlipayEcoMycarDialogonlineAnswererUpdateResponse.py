#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarDialogonlineAnswererUpdateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarDialogonlineAnswererUpdateResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarDialogonlineAnswererUpdateResponse, self).parse_response_content(response_content)
