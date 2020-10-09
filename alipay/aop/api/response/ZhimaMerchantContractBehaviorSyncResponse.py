#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantContractBehaviorSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantContractBehaviorSyncResponse, self).__init__()
        self._out_biz_no = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantContractBehaviorSyncResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
