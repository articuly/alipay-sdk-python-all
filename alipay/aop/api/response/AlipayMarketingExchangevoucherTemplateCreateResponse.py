#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingExchangevoucherTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingExchangevoucherTemplateCreateResponse, self).__init__()
        self._template_id = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingExchangevoucherTemplateCreateResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
