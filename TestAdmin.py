# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:03:53 2018

@author: Lester
"""

import unittest
from BusinessLogic.Admin import Admin

class TestAdmin(unittest.TestCase):
    admin1 = Admin('001', 'Lester', 'Nuñez', 'Manuel')
    admin2 = Admin('002', 'Vince Harley', 'De Jesus', 'Gaba')    

    def test_correct__eq__(self):
        self.assertEqual(TestAdmin.admin1.__eq__(TestAdmin.admin1), True)
        self.assertEqual(TestAdmin.admin2.__eq__(TestAdmin.admin2), True)        

    def test_wrong__eq__(self):
        self.assertEqual(TestAdmin.admin1.__eq__(TestAdmin.admin1), True)
        self.assertEqual(TestAdmin.admin2.__eq__(TestAdmin.admin1), False)
