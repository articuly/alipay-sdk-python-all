#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppApiresQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppApiresQueryResponse, self).__init__()
        self._item_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppApiresQueryResponse, self).parse_response_content(response_content)
        if 'item_id' in response:
            self.item_id = response['item_id']
