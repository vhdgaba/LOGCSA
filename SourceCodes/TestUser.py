# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:00:18 2018

@author: Lester
"""

import unittest
from BusinessLogic.User import User, Student, Advisee, PeerAdviser, Admin

class TestUser(unittest.TestCase):
    user1 = User('Lester', 'Nuñez', 'Manuel')
    user2 = User('Vince Harley', 'De Jesus', 'Gaba')
    
    def test_correct_get_fullname(self):
        self.assertEqual(TestUser.user1.get_fullname(), 'Manuel, Lester Nuñez')
        self.assertEqual(TestUser.user2.get_fullname(), 'Gaba, Vince Harley De Jesus')
              
    def test_wrongformat_get_fullname(self):
        self.assertEqual(TestUser.user1.get_fullname(), 'Manuel, Lester Nuñez')
        self.assertEqual(TestUser.user1.get_fullname(), 'Lester Nuñez Manuel')
        
    def test_nocomma_get_fullname(self):
        self.assertEqual(TestUser.user2.get_fullname(), 'Gaba, Vince Harley De Jesus')
        self.assertEqual(TestUser.user2.get_fullname(), 'Gaba Vince Harley De Jesus')
        
    def test_wrong_get_fullname(self):
        self.assertEqual(TestUser.user1.get_fullname(), 'Manuel, Lester Nunez')
        self.assertEqual(TestUser.user2.get_fullname(), 'Gabo, Vince Harley De Jesus')
      
class TestStudent(unittest.TestCase):
    student1 = Student(2015103119, 'Lester', 'Nuñez', 'Manuel', 'CPE', '09498835973')
    student2 = Student(2015102105, 'Vince Harley', 'De Jesus', 'Gaba', 'CPE', '09082115561')    
    
class TestAdvisee(unittest.TestCase):
    advisee1 = Advisee(2015103119, 'Lester', 'Nuñez', 'Manuel', 'CPE', '09498835973', 'B51 L12 Dreamland Subdivision, Brgy. Hagonoy, Taguig, Metro Manila', 'lnmanuel@mymail.mapua.edu.ph')
    advisee2 = Advisee(2015102105, 'Vince Harley', 'De Jesus', 'Gaba', 'CPE', '09082115561', '1048-C Solis Street, Tondo, Manila, Metro Manila', 'vhdgaba@mymail.mapua.edu.ph')    

class TestPeerAdviser(unittest.TestCase):
    peer1 = PeerAdviser(2015103119, 'Lester', 'Nuñez', 'Manuel', 'CPE', '09498835973', 'HSM')
    peer2 = PeerAdviser(2015102105, 'Vince Harley', 'De Jesus', 'Gaba', 'CPE', '09082115561', 'HSM')

class TestAdmin(unittest.TestCase):
    admin1 = Admin('001', 'Lester', 'Nuñez', 'Manuel')
    admin2 = Admin('002', 'Vince Harley', 'De Jesus', 'Gaba')
    
    def test_correct__eq__(self):
        self.assertEqual(TestAdmin.admin1.__eq__(TestAdmin.admin1), True)
        self.assertEqual(TestAdmin.admin2.__eq__(TestAdmin.admin2), True)
        
    def test_wrong__eq__(self):
        self.assertEqual(TestAdmin.admin1.__eq__(TestAdmin.admin1), True)
        self.assertEqual(TestAdmin.admin2.__eq__(TestAdmin.admin1), True)
        
    
        
if __name__ == '__main__':
    unittest.main()