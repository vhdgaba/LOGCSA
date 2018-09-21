#  The program searches for a string in an array and return location index if found.  

class search:    
    def __init__(self):
        self.usernames = []
    def search(username, usernames : []):
        if username in usernames:
            return usernames.index(username)
        else:
            return 'not found'
