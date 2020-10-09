#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneHealthActivitySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneHealthActivitySyncResponse, self).__init__()
        self._apply_no = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneHealthActivitySyncResponse, self).parse_response_content(response_content)
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
