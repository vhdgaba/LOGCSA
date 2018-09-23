from FileHandler import FileHandler
from User import Advisee, PeerAdviser, Admin
import hashlib

fh = FileHandler('datatry.db')
errormsg = 'No error'

class Session:
    def __init__(self):
        self.admin = None
        self.advisees = []
        self.peeradvisers = []
        self.adviseecount = 0
        self.peeradvisercount = 0

    def login_advisee(self, studentnumber):
        global errormsg
        if fh.in_advisee(studentnumber):
            user = Advisee(*fh.get_advisee(studentnumber))
            if user in self.advisees:
                errormsg = 'Duplicate Error: The account is already logged in.'
                return False
            else:
                self.advisees.append(user)
                self.adviseecount += 1
                errormsg = 'No error'
                return True
        else:
            errormsg = 'The login ID did not match any record.'
            return False
        
    def login_peeradviser(self, studentnumber, password):
        global errormsg
        if fh.in_peeradviser(studentnumber):
            truepassword, = fh.get_password(studentnumber)
            if str(studentnumber)[:4] == '9999':
                errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
            elif self.check_password(truepassword, password):
                user = PeerAdviser(*fh.get_peeradviser(studentnumber))
                if user in self.peeradvisers:
                    errormsg = 'Duplicate Error: The account is already logged in.'
                    return False
                else:
                    self.peeradvisers.append(user)
                    self.peeradvisercount += 1
                    errormsg = 'No error'
                    return True
            else:
                errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
        else:
            errormsg = 'Login Error: The login ID and password entered did not match any record.'
            return False

    def login_admin(self, adminid, password):
        global errormsg
        if fh.in_admin(adminid):
            truepassword, = fh.get_password(adminid)
            if str(adminid)[:4] != '9999':
                errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
            elif self.check_password(truepassword, password):
                self.admin = Admin(*fh.get_admin(adminid))
                errormsg = 'No error'
                return True
            else:
                errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
        else:
            errormsg = 'Login Error: The login ID and password entered did not match any record.'
            return False
    
    def logout_advisee(self, advisee):
        self.advisees.remove(advisee)
        self.adviseecount -= 1

    def logout_peeradviser(self, peeradviser):
        self.peeradvisers.remove(peeradviser)
        self.peeradvisercount -= 1
        
    def logout_admin(self, admin):
        self.admin = None
    
#    def register_advisee(self):
    #add advisee
  
#    def register_peer_adviser(self):
    #add peeradviser, add login
    
#    def end_session(self)
    #set null timeouts to placeholder value
    

    #Check if password matches the hashed password. Reference: https://www.pythoncentral.io/hashing-strings-with-python/  
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split('g')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

if __name__ == '__main__':
    pass
    