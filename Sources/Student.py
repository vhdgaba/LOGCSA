from FileHandler import FileHandler


class Session:
    def __init__(self, database):
        self.fh = FileHandler(database)
        self.admins = []
        self.advisees = []
        self.peeradvisers = []
        self.admincount = 0
        self.adviseecount = 0
        self.peeradvisercount = 0
        
    #In progress
#    def login(self, accountid, password):
#        truepassword, = self.fh.get_password(accountid)
#        if password == truepassword:
#            print("Logged In")
#            return True
#        else:
#            print("Failed")
#            return False

class User:
    def __init__(self, firstname = '', middlename = '', lastname = ''):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
    
class Admin(User):
    def __init__(self, adminid, firstname, middlename, lastname):
        User.__init__(firstname, middlename, lastname)
        self.adminid = adminid

class Student(User):
    def __init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber):
        User.__init__(self, firstname, middlename, lastname)
        self.studentnumber = studentnumber
        self.program = program
        self.contactnumber = contactnumber
    
    def get_fullname(self):
        return "{}, {} {}".format(self.lastname, self.firstname, self.middlename)

    #Returns the full name of the student as a printable representation of the object
    def __str__(self):
        return self.get_fullname()

class Advisee(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.homeaddress = homeaddress
    
    
class PeerAdviser(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, organization):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.organization = organization
        
        
if __name__ == "__main__":
   # sesh = Session('datatry.db')
   # sesh.login(2015103119,'letmein')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    