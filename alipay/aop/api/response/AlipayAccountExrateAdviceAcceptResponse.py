#!/usr/bin/env python
# -*- coding: utf-8 -*-
import simplejson as json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountExrateAdviceAcceptResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateAdviceAcceptResponse, self).__init__()
        self._client_id = None
        self._contra_amount = None
        self._contra_ccy = None
        self._deal_ref = None
        self._dealt_rate = None
        self._duplicate = None
        self._messag_id = None
        self._msg_type = None
        self._requested_rate_status = None
        self._side = None
        self._transaction_amount = None
        self._transaction_ccy = None
        self._value_date = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def contra_amount(self):
        return self._contra_amount

    @contra_amount.setter
    def contra_amount(self, value):
        self._contra_amount = value
    @property
    def contra_ccy(self):
        return self._contra_ccy

    @contra_ccy.setter
    def contra_ccy(self, value):
        self._contra_ccy = value
    @property
    def deal_ref(self):
        return self._deal_ref

    @deal_ref.setter
    def deal_ref(self, value):
        self._deal_ref = value
    @property
    def dealt_rate(self):
        return self._dealt_rate

    @dealt_rate.setter
    def dealt_rate(self, value):
        self._dealt_rate = value
    @property
    def duplicate(self):
        return self._duplicate

    @duplicate.setter
    def duplicate(self, value):
        self._duplicate = value
    @property
    def messag_id(self):
        return self._messag_id

    @messag_id.setter
    def messag_id(self, value):
        self._messag_id = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value
    @property
    def requested_rate_status(self):
        return self._requested_rate_status

    @requested_rate_status.setter
    def requested_rate_status(self, value):
        self._requested_rate_status = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
    @property
    def transaction_amount(self):
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, value):
        self._transaction_amount = value
    @property
    def transaction_ccy(self):
        return self._transaction_ccy

    @transaction_ccy.setter
    def transaction_ccy(self, value):
        self._transaction_ccy = value
    @property
    def value_date(self):
        return self._value_date

    @value_date.setter
    def value_date(self, value):
        self._value_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateAdviceAcceptResponse, self).parse_response_content(response_content)
        if 'client_id' in response:
            self.client_id = response['client_id']
        if 'contra_amount' in response:
            self.contra_amount = response['contra_amount']
        if 'contra_ccy' in response:
            self.contra_ccy = response['contra_ccy']
        if 'deal_ref' in response:
            self.deal_ref = response['deal_ref']
        if 'dealt_rate' in response:
            self.dealt_rate = response['dealt_rate']
        if 'duplicate' in response:
            self.duplicate = response['duplicate']
        if 'messag_id' in response:
            self.messag_id = response['messag_id']
        if 'msg_type' in response:
            self.msg_type = response['msg_type']
        if 'requested_rate_status' in response:
            self.requested_rate_status = response['requested_rate_status']
        if 'side' in response:
            self.side = response['side']
        if 'transaction_amount' in response:
            self.transaction_amount = response['transaction_amount']
        if 'transaction_ccy' in response:
            self.transaction_ccy = response['transaction_ccy']
        if 'value_date' in response:
            self.value_date = response['value_date']
