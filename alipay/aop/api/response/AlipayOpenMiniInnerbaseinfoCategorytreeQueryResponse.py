#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MiniAppFirstCategoryInfo import MiniAppFirstCategoryInfo


class AlipayOpenMiniInnerbaseinfoCategorytreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoCategorytreeQueryResponse, self).__init__()
        self._category_list = None

    @property
    def category_list(self):
        return self._category_list

    @category_list.setter
    def category_list(self, value):
        if isinstance(value, list):
            self._category_list = list()
            for i in value:
                if isinstance(i, MiniAppFirstCategoryInfo):
                    self._category_list.append(i)
                else:
                    self._category_list.append(MiniAppFirstCategoryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerbaseinfoCategorytreeQueryResponse, self).parse_response_content(response_content)
        if 'category_list' in response:
            self.category_list = response['category_list']
