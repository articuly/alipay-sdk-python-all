#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringEleOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringEleOrderSyncResponse, self).__init__()
        self._order_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringEleOrderSyncResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
