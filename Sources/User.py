from FileHandler import FileHandler

userfh = FileHandler('datatry.db')
usererrormsg = 'No error'


class User:
    def __init__(self, firstname = '', middlename = '', lastname = ''):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        
    #Returns the full name of the user as a printable representation of the object
    def __str__(self):
        return self.get_fullname()
    
    def __repr__(self):
        return "User({},{},{})".format(self.firstname, self.middlename, self.lastname)
    
    def get_fullname(self):
        return "{}, {} {}".format(self.lastname, self.firstname, self.middlename)
    
class Student(User):
    def __init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber):
        User.__init__(self, firstname, middlename, lastname)
        self.studentnumber = studentnumber
        self.program = program
        self.contactnumber = contactnumber
    
    def __eq__(self, other):
        try:
            return self.studentnumber == other.studentnumber
        except:
            return False

class Advisee(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.homeaddress = homeaddress
    
    def time_in(self, subject, adviser):
        userfh.advisee_timein(self.studentnumber, subject, adviser)
        
    def time_out(self):
        userfh.advisee_timeout(self.studentnumber)
    
class PeerAdviser(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, organization):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.organization = organization
    
    def time_in(self, subject, adviser):
        userfh.peeradviser_timein(self.studentnumber)
        
    def time_out(self):
        userfh.peeradviser_timeout(self.studentnumber)

class Admin(User):
    def __init__(self, adminid, firstname, middlename, lastname):
        User.__init__(self, firstname, middlename, lastname)
        self.adminid = adminid
        
    def __eq__(self, other):
        try:
            return self.adminid == other.adminid
        except:
            return False

    def remove_advisee(self, studentnumber, session):
        global usererrormsg
        user = Advisee(*userfh.get_advisee(studentnumber))
        if user in session.advisees:
            usererrormsg = 'Error: Cannot delete user while in session.'  
            return False
        else:
            userfh.remove_advisee(studentnumber)
            return True
        
    def remove_peeradviser(self, studentnumber, session):
        global usererrormsg
        user = PeerAdviser(*userfh.get_peeradviser(studentnumber))
        if user in session.peeradvisers:
            usererrormsg = 'Error: Cannot delete user while in session.'  
            return False
        else:
            userfh.remove_advisee(studentnumber)
            return True
        
    def remove_admin(self, adminid):
        userfh.remove_admin(adminid)
        
#    def register_admin
    
#    def get_timesheet

#    def get_sessionlog

#    def update_advisee

#    def update_peeradviser

#    def update_admin

#    def update_sessionlog

#    def update_timesheet 
    
#    def get_peeradviserpoints