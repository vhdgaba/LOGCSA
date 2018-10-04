# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:48:21 2018

@author: Lester
"""

import unittest
from BusinessLogic.Session import Session
from DataAccess.FileHandler import FileHandler

class TestSession(unittest.TestCase):
    session1 = Session
    session1.peeradvisercount = 0
    
    def test_login_peeradviser(self):
        TestSession.session1.peeradvisercount = 0
        self.assertEqual(TestSession.session1.login_advisee(self, 2015103119), True)
        
if __name__ == '__main__':
    unittest.main()