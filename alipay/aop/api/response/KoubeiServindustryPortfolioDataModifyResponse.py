#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryPortfolioDataModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPortfolioDataModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPortfolioDataModifyResponse, self).parse_response_content(response_content)
