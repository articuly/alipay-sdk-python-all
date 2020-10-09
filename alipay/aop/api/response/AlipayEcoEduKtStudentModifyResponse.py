#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduKtStudentModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtStudentModifyResponse, self).__init__()
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtStudentModifyResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
