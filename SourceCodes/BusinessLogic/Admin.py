from DataAccess.FileHandler import FileHandler
from BusinessLogic.User import User
from BusinessLogic.Advisee import Advisee
from BusinessLogic.PeerAdviser import PeerAdviser
import datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

userfh = FileHandler('../Data/record.db')

class Admin(User):
    def __init__(self, adminid, firstname, middlename, lastname, emailaddress):
        User.__init__(self, firstname, middlename, lastname, emailaddress)
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

    def register_admin(self, adminid, firstname, middlename, lastname, password, confirmpassword, email):
        if userfh.in_admin(adminid):
            self.errormsg = 'Error: Username already taken'
            return False
        elif len(password) < 6:
            self.errormsg = 'Error: Password must be at least 6 characters'
            return False
        elif password != confirmpassword:
            self.errormsg = 'Error: Your password and confirm password do not match'
            return False
        else:
            newuser = Admin(adminid, firstname, middlename, lastname, email)
            userfh.add_admin(newuser)
            userfh.register_user(adminid, password)
            self.errormsg = 'No error'
            return True

    def register_peeradviser(self, studentnumber, firstname, middlename, lastname, program, contactnumber, organization, emailaddress, password, dayone, timeone, daytwo, timetwo):
        latestyear = int(datetime.datetime.now().strftime("%Y"))
        try:
            studentnumber = int(studentnumber)
        except:
            self.errormsg = 'Error: Invalid student number'
            return False
        else:
            try:
                int(contactnumber)
                if len(contactnumber) != 11:
                    raise
            except:
                self.errormsg = 'Error: Invalid contact number'
            else:
                if str(studentnumber)[:4] == '9999' or len(str(studentnumber)) != 10:
                    self.errormsg = 'Error: Invalid student number'
                    return False
                elif userfh.in_peeradviser(studentnumber):
                    self.errormsg = 'Error: Student Number already taken'
                else:
                    year = int(studentnumber/1000000)
                    if year in range(2000, latestyear + 1):
                        if len(password) < 6:
                            self.errormsg = 'Error: Password must be at least 6 characters'
                            return False
                        elif emailaddress[-20:] != '@mymail.mapua.edu.ph':
                            self.errormsg = 'Error: Invalid email address'
                            return False
                        elif dayone == daytwo and timeone == timetwo:
                            self.errormsg = 'Error: Advising schedules must be distinct'
                            return False
                        else:
                            newuser = PeerAdviser(studentnumber, firstname, middlename, lastname, program, contactnumber, organization, emailaddress)
                            userfh.register_user(studentnumber, password)
                            userfh.add_peeradviser(newuser)
                            userfh.add_schedule(studentnumber, dayone, timeone, daytwo, timetwo)
                            self.errormsg = 'No error'
                            return True
                    else:
                        self.errormsg = 'Error: Invalid student number'
                        return False

    def email_adviser(self, password, subject_text, content_text):
        failed = 0
        for email, in userfh.get_emailadviser():
            print(email)
            msg = MIMEMultipart()
            msg['From'] = self.emailaddress
            msg['To'] = email
            msg['Subject'] = subject_text
            
            content = content_text
            msg.attach(MIMEText(content, 'plain'))
            
            content = msg.as_string()
            server = smtplib.SMTP('smtp-mail.outlook.com:587')
            
            try:
                server.starttls()
                server.login(self.emailaddress, password)
                
                server.sendmail(self.emailaddress, email, content)
                server.quit()
            except:
                failed += 1
        return failed
    
    def email_advisee(self, password, subject_text, content_text):
        failed = 0
        for email, in userfh.get_emailadvisee():
            msg = MIMEMultipart()
            msg['From'] = self.emailaddress
            msg['To'] = email
            msg['Subject'] = subject_text
            
            content = content_text
            msg.attach(MIMEText(content, 'plain'))
            
            content = msg.as_string()
            server = smtplib.SMTP('smtp-mail.outlook.com:587')
            
            try:
                server.starttls()
                server.login(self.emailaddress, password)
                
                server.sendmail(self.emailaddress, email, content)
                server.quit()
            except:
                failed += 1
        return failed
            
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

    def clear_database(self):
        userfh.clear_database()
    
if __name__ == '__main__':
    pass