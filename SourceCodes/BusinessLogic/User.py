import sys
sys.path.append('../')
from DataAccess.FileHandler import FileHandler
import datetime

userfh = FileHandler('Data/record.db')
defaultsubjecttitle = 'General Information'

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
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress, emailaddress):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.homeaddress = homeaddress
        self.emailaddress = emailaddress

    def time_in(self, subject, adviser):
        if subject == '':
            subject = defaultsubjecttitle
        userfh.advisee_timein(self.studentnumber, subject, adviser)

    def time_out(self):
        userfh.advisee_timeout(self.studentnumber)

class PeerAdviser(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, organization):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.organization = organization

    def time_in(self):
        userfh.peeradviser_timein(self.studentnumber)

    def time_out(self):
        userfh.peeradviser_timeout(self.studentnumber)

class Admin(User):
    def __init__(self, adminid, firstname, middlename, lastname):
        User.__init__(self, firstname, middlename, lastname)
        self.adminid = adminid
        self.errormsg = 'No error'

    def __eq__(self, other):
        try:
            return self.adminid == other.adminid
        except:
            return False

    def remove_advisee(self, studentnumber, session):
        user = Advisee(*userfh.get_advisee(studentnumber))
        if user in session.advisees:
            self.errormsg = 'Error: Cannot delete user while in session.'
            return False
        else:
            userfh.remove_advisee(studentnumber)
            return True

    def remove_peeradviser(self, studentnumber, session):
        user = PeerAdviser(*userfh.get_peeradviser(studentnumber))
        if user in session.peeradvisers:
            self.errormsg = 'Error: Cannot delete user while in session.'
            return False
        else:
            userfh.remove_advisee(studentnumber)
            return True

    def remove_admin(self, adminid):
        userfh.remove_admin(adminid)

    def register_admin(self, adminid, firstname, middlename, lastname, password, confirmpassword):
        try:
            adminid = int(adminid)
        except:
            self.errormsg = 'Error: Invalid admin ID'
            return False
        else:
            if str(adminid)[:4] != '9999' or len(str(adminid)) != 10:
                self.errormsg = 'Error: Invalid student number'
                return False
            else:
                if len(password) < 6:
                    self.errormsg = 'Error: Password must be at least 6 characters'
                    return False
                elif password != confirmpassword:
                    self.errormsg = 'Error: Your password and confirm password do not match'
                    return False
                else:
                    newuser = Admin(adminid, firstname, middlename, lastname)
                    userfh.add_admin(newuser)
                    self.errormsg = 'No error'
                    return True

    def register_peeradviser(self, studentnumber, firstname, middlename, lastname, program, contactnumber, organization, password, confirmpassword):
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
            else:
                year = int(studentnumber/1000000)
                if year in range(2000, latestyear + 1):
                    if len(password) < 6:
                        self.errormsg = 'Error: Password must be at least 6 characters'
                        return False
                    elif password != confirmpassword:
                        self.errormsg = 'Error: Your password and confirm password do not match'
                        return False
                    else:
                        newuser = PeerAdviser(studentnumber, firstname, middlename, lastname, program, contactnumber, organization)
                        userfh.add_peeradviser(newuser)
                        self.errormsg = 'No error'
                        return True
                else:
                    self.errormsg = 'Error: Invalid student number'
                    return False

    def update_advisee(self, newstudentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress, emailaddress, currentstudentnumber):
        latestyear = int(datetime.datetime.now().strftime("%Y"))
        try:
            newstudentnumber = int(newstudentnumber)
        except:
            self.errormsg = 'Error: Invalid student number'
            return False
        else:
            if str(newstudentnumber)[:4] == '9999' or len(str(newstudentnumber)) != 10:
                self.errormsg = 'Error: Invalid student number'
                return False
            elif emailaddress[-20:] != '@mymail.mapua.edu.ph':
                self.errormsg = 'Error: Invalid email address'
                return False
            else:
                year = int(newstudentnumber/1000000)
                if year in range(2000, latestyear + 1):
                    updateduser = Advisee(newstudentnumber, firstname, middlename, lastname, program, contactnumber, homeaddress, emailaddress)
                    userfh.update_advisee(currentstudentnumber, updateduser)
                    self.errormsg = 'No error'
                    return True
                else:
                    self.errormsg = 'Error: Invalid student number'
                    return False

    def update_peeradviser(self, newstudentnumber, firstname, middlename, lastname, program, contactnumber, organization, password, confirmpassword, currentstudentnumber):
        latestyear = int(datetime.datetime.now().strftime("%Y"))
        try:
            newstudentnumber = int(newstudentnumber)
        except:
            self.errormsg = 'Error: Invalid student number'
            return False
        else:
            if str(newstudentnumber)[:4] == '9999' or len(str(newstudentnumber)) != 10:
                self.errormsg = 'Error: Invalid student number'
                return False
            else:
                year = int(newstudentnumber/1000000)
                if year in range(2000, latestyear + 1):
                    if len(password) < 6:
                        self.errormsg = 'Error: Password must be at least 6 characters'
                        return False
                    elif password != confirmpassword:
                        self.errormsg = 'Error: Your password and confirm password do not match'
                        return False
                    else:
                        newuser = PeerAdviser(newstudentnumber, firstname, middlename, lastname, program, contactnumber, organization)
                        userfh.update_peeradviser(currentstudentnumber, newuser)
                        self.errormsg = 'No error'
                        return True
                else:
                    self.errormsg = 'Error: Invalid student number'
                    return False

    def update_admin(self, newadminid, firstname, middlename, lastname, password, confirmpassword, currentadminid):
        global usererrormsg
        try:
            newadminid = int(newadminid)
        except:
            self.errormsg = 'Error: Invalid admin ID'
            return False
        else:
            if str(newadminid)[:4] != '9999' or len(str(newadminid)) != 10:
                self.errormsg = 'Error: Invalid student number'
                return False
            else:
                if len(password) < 6:
                    self.errormsg = 'Error: Password must be at least 6 characters'
                    return False
                elif password != confirmpassword:
                    self.errormsg = 'Error: Your password and confirm password do not match'
                    return False
                else:
                    newuser = Admin(newadminid, firstname, middlename, lastname)
                    userfh.update_admin(currentadminid, newuser)
                    self.errormsg = 'No error'
                    return True

    def get_studenttimesheet(self, studentnumber):
        return userfh.get_studenttimesheet(studentnumber)

    def get_studentsessionlog(self, studentnumber):
        return userfh.get_studentsessionlog(studentnumber)

    def get_dailytimesheet(self, date):
        return userfh.get_dailytimesheet(date)

    def get_dailysessionlog(self, date):
        return userfh.get_dailysessionlog(date)

    def get_session(self, logid):
        return userfh.get_session(logid)

    def get_timelog(self, logid):
        return userfh.get_timelog(logid)

    def update_sessionlog(self, logid, timein, timeout, subject, adviserid):
        userfh.update_sessionlog(logid, timein, timeout, subject, adviserid)

    def update_timesheet(self, logid, timein, timeout):
        userfh.update_timesheet(logid, timein, timeout)
        
    def add_subject(self, subject):
        userfh.add_subject(subject)
    
    def remove_subject(self, subject):
        userfh.remove_subject(subject)

    def get_peeradviserpoints(self, studentnumber):
        self.get_studenttimesheet(studentnumber)

if __name__ == '__main__':
    pass