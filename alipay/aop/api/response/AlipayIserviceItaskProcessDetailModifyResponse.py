#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtendFieldInfo import ExtendFieldInfo


class AlipayIserviceItaskProcessDetailModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskProcessDetailModifyResponse, self).__init__()
        self._alipay_process_id = None
        self._alipay_process_status = None
        self._extend_field_infos = None

    @property
    def alipay_process_id(self):
        return self._alipay_process_id

    @alipay_process_id.setter
    def alipay_process_id(self, value):
        self._alipay_process_id = value
    @property
    def alipay_process_status(self):
        return self._alipay_process_status

    @alipay_process_status.setter
    def alipay_process_status(self, value):
        self._alipay_process_status = value
    @property
    def extend_field_infos(self):
        return self._extend_field_infos

    @extend_field_infos.setter
    def extend_field_infos(self, value):
        if isinstance(value, list):
            self._extend_field_infos = list()
            for i in value:
                if isinstance(i, ExtendFieldInfo):
                    self._extend_field_infos.append(i)
                else:
                    self._extend_field_infos.append(ExtendFieldInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskProcessDetailModifyResponse, self).parse_response_content(response_content)
        if 'alipay_process_id' in response:
            self.alipay_process_id = response['alipay_process_id']
        if 'alipay_process_status' in response:
            self.alipay_process_status = response['alipay_process_status']
        if 'extend_field_infos' in response:
            self.extend_field_infos = response['extend_field_infos']
