from FileHandler import FileHandler
from User import Advisee, PeerAdviser, Admin
import hashlib, datetime

fh = FileHandler('record.db')

class Session:
    def __init__(self):
        self.admin = None
        self.advisees = []
        self.peeradvisers = []
        self.adviseecount = 0
        self.peeradvisercount = 0
        self.errormsg = 'No error'

    def get_subjects(self):
        return fh.get_subjects()
    
    def get_subject(self, subjectid):
        return fh.get_subject(subjectid)

    def login_advisee(self, studentnumber):
        if self.peeradvisercount == 0:
            self.errormsg = 'Error: Advisee cannot log in if there are no peer advisers in session.'
            return False
        elif fh.in_advisee(studentnumber):
            user = Advisee(*fh.get_advisee(studentnumber))
            if user in self.advisees:
                self.errormsg = 'Duplicate Error: The account is already logged in.'
                return False
            else:
                self.advisees.append(user)
                self.adviseecount += 1
                self.errormsg = 'No error'
                return True
        else:
            self.errormsg = 'Error: The login ID did not match any record.'
            return False

    def login_peeradviser(self, studentnumber, password):
        if fh.in_peeradviser(studentnumber):
            truepassword, = fh.get_password(studentnumber)
            if str(studentnumber)[:4] == '9999':
                self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
            elif self.check_password(truepassword, password):
                user = PeerAdviser(*fh.get_peeradviser(studentnumber))
                if user in self.peeradvisers:
                    self.errormsg = 'Duplicate Error: The account is already logged in.'
                    return False
                else:
                    self.peeradvisers.append(user)
                    self.peeradvisercount += 1
                    self.errormsg = 'No error'
                    return True
            else:
                self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
        else:
            self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
            return False

    def login_admin(self, adminid, password):
        if fh.in_admin(adminid):
            truepassword, = fh.get_password(adminid)
            if str(adminid)[:4] != '9999':
                self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
            elif self.check_password(truepassword, password):
                self.admin = Admin(*fh.get_admin(adminid))
                self.errormsg = 'No error'
                return True
            else:
                self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
                return False
        else:
            self.errormsg = 'Login Error: The login ID and password entered did not match any record.'
            return False

    def logout_advisee(self, advisee):
        self.advisees.remove(advisee)
        self.adviseecount -= 1

    def logout_peeradviser(self, peeradviser):
        self.peeradvisers.remove(peeradviser)
        self.peeradvisercount -= 1

    def logout_admin(self, admin):
        self.admin = None

    def register_advisee(self, studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress):
        latestyear = int(datetime.datetime.now().strftime("%Y"))
        try:
            studentnumber = int(studentnumber)
        except:
            self.errormsg = 'Error: Invalid student number'
            return False
        else:
            if str(studentnumber)[:4] == '9999' or len(str(studentnumber)) != 10:
                self.errormsg = 'Error: Invalid student number'
                return False
            elif fh.in_advisee(studentnumber):
                self.errormsg = 'Error: Student number already registered.'
                return False
            else:
                year = int(studentnumber/1000000)
                if year in range(2000, latestyear + 1):
                    newuser = Advisee(studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress)
                    fh.add_advisee(newuser)
                    self.errormsg = 'No error'
                    return True
                else:
                    self.errormsg = 'Error: Invalid student number'
                    return False

    def end_session(self):
        fh.terminate_nulls()
        fh.close()

    #Check if password matches the hashed password. Reference: https://www.pythoncentral.io/hashing-strings-with-python/
    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split('g')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

if __name__ == '__main__':
    pass