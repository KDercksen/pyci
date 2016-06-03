#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import Mock


class TestServer(TestCase):

    def setUp(self):
        self.handler = Mock()
        self.handler.respond.return_value = 3

    def tearDown(self):
        self.handler = None

    def test_respond_return(self):
        v = self.handler.respond('some data')
        self.assertEquals(v, 3)
