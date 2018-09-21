# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:56:21 2018
@author: Lester Manuel
"""
#  The program searches for a string in an array and return location index if found.  

class Search:    
    def __init__(self):
        self.usernames = []
    def search(username, usernames : []):
        if username in usernames:
            return usernames.index(username)
        else:
            return None
