# -*- coding: utf-8 -*-

import unittest
import os
from api.testDAL import appCase as ac

PATH = lambda p: os.path.abspath(
       os.path.join(os.path.dirname(__file__), p)
 )


class TestCase(unittest.TestCase):

    def test_login(self):
        home_yaml = PATH("../Case/login.yaml")
        ac.AppCase.execCase(self, f=home_yaml)