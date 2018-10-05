# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:48:21 2018

@author: Lester
"""


#2015103119 - adviser
#2015102105 - adviser
#2015100895 - adviser
#2018999999 - student
#2017123123 - student
#2017123124 - student

import unittest
from BusinessLogic.Session import Session
from DataAccess.FileHandler import FileHandler

class TestSession(unittest.TestCase):
    session1 = Session()    

    ##### --Test login_advisee()-- #####
    def test_login_advisee_no_peeradviser(self):
        TestSession.session1.peeradvisercount = 0
        self.assertEqual(TestSession.session1.login_advisee(2018999999), True)

    def test_registeredsn_login_advisee(self):
        TestSession.session1.peeradvisercount = 1
        self.assertEqual(TestSession.session1.login_advisee(2017123123), True)

    def test_loggedregisteredsn_login_advisee(self):
        TestSession.session1.peeradvisercount = 1
        self.assertEqual(TestSession.session1.login_advisee(2018999999), True)
        self.assertEqual(TestSession.session1.login_advisee(2018999999), True)

    def test_unregistesredsn_login_advisee(self):
        TestSession.session1.peeradvisercount = 1
        self.assertEqual(TestSession.session1.login_advisee(2015103119), True)    

    ##### --Test login_peeradviser()-- #####

    def test_wsnwpw_login_peeradviser(self):
        self.assertEqual(TestSession.session1.login_peeradviser(2015103115, "hi"), True)

    def test_wsncpw_login_peeradviser(self):
        self.assertEqual(TestSession.session1.login_peeradviser(2015103115, "lester"), True)

    def test_csnwpw_login_peeradviser(self):
        self.assertEqual(TestSession.session1.login_peeradviser(2015103119, "password"), True)

    def test_csncpw_login_peeradviser(self):
        self.assertEqual(TestSession.session1.login_peeradviser(2015103119, "lester"), True)

    def test_logged_login_peeradviser(self):
        self.assertEqual(TestSession.session1.login_peeradviser(2015102105, "vince"), True)
        self.assertEqual(TestSession.session1.login_peeradviser(2015102105, "vince"), True)
    

if __name__ == '__main__':
    unittest.main()