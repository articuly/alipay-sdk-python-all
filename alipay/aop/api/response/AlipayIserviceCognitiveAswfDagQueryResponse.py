#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveAswfDagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveAswfDagQueryResponse, self).__init__()
        self._dag_id = None
        self._error_code = None
        self._error_msg = None
        self._success = None

    @property
    def dag_id(self):
        return self._dag_id

    @dag_id.setter
    def dag_id(self, value):
        self._dag_id = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveAswfDagQueryResponse, self).parse_response_content(response_content)
        if 'dag_id' in response:
            self.dag_id = response['dag_id']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'success' in response:
            self.success = response['success']
