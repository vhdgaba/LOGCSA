import sqlite3, datetime
import uuid, hashlib

placeholder = 'x'

class FileHandler:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.cs = self.db.cursor()
        try:
            self.create_database()
        except:
            pass

    def create_database(self):
        self.cs.execute('CREATE TABLE Login(AccountID text primary key, Password text)')
        self.cs.execute('CREATE TABLE Admin(AdminID text primary key, FirstName text, MiddleName text, LastName text, EmailAddress Text)')
        self.cs.execute('CREATE TABLE Advisee(StudentNumber integer primary key, FirstName text, MiddleName text, LastName text, Program text, ContactNumber text, HomeAddress text, EmailAddress text)')
        self.cs.execute('CREATE TABLE PeerAdviser(StudentNumber integer primary key, FirstName text, MiddleName text, LastName text, Program text, ContactNumber text, Organization text, EmailAddress text)')
        self.cs.execute('CREATE TABLE SessionLog(LogID integer primary key autoincrement, StudentNumber integer, Date text, TimeIn text, TimeOut text, Subject text, AdviserID integer)')
        self.cs.execute('CREATE TABLE TimeSheet(LogID integer primary key autoincrement, StudentNumber integer, Date text, TimeIn text, TimeOut text)')
        self.cs.execute('CREATE TABLE Subject(Code text primary key, Title text, Field text)')
        self.cs.execute('CREATE TABLE AdvisingSchedule(StudentNumber integer primary key, DayOne text, TimeOne text, DayTwo text, TimeTwo, text)')

    def clear_database(self):
        self.cs.execute('DELETE FROM Login')
        self.cs.execute('DELETE FROM Advisee')
        self.cs.execute('DELETE FROM PeerAdviser')
        self.cs.execute('DELETE FROM SessionLog')
        self.cs.execute('DELETE FROM TimeSheet')
        self.cs.execute('DELETE FROM AdvisingSchedule')
        self.cs.execute('DELETE FROM sqlite_sequence')
        self.cs.execute('VACUUM')

    def add_subject(self, code, title, field):
        with self.db:
            self.cs.execute("INSERT INTO Subject VALUES(?,?,?)", code, title, field)

    def add_advisee(self, advisee):
        with self.db:
            self.cs.execute("INSERT INTO Advisee VALUES(?,?,?,?,?,?,?,?)", (advisee.studentnumber, advisee.firstname, advisee.middlename, advisee.lastname, advisee.program, advisee.contactnumber, advisee.homeaddress, advisee.emailaddress))

    def add_peeradviser(self, peeradviser):
        with self.db:
            self.cs.execute("INSERT INTO PeerAdviser VALUES(?,?,?,?,?,?,?,?)", (peeradviser.studentnumber, peeradviser.firstname, peeradviser.middlename, peeradviser.lastname, peeradviser.program, peeradviser.contactnumber, peeradviser.organization, peeradviser.emailaddress))

    def add_admin(self, admin):
        with self.db:
            self.cs.execute("INSERT INTO Admin VALUES(?,?,?,?,?)", (admin.adminid, admin.firstname, admin.middlename, admin.lastname, admin.emailaddress))

    def add_schedule(self, studentnumber, dayone, timeone, daytwo, timetwo):
        with self.db:
            self.cs.execute("INSERT INTO AdvisingSchedule VALUES(?,?,?,?,?)",(studentnumber, dayone, timeone, daytwo, timetwo))

    def remove_subject(self, code):
        with self.db:
            self.cs.execute("DELETE FROM Subject WHERE Code=?",(code,))

    def remove_advisee(self, studentnumber):
        with self.db:
            self.cs.execute("DELETE FROM Advisee WHERE StudentNumber=?",(studentnumber,))

    def remove_peeradviser(self, studentnumber):
        with self.db:
            self.cs.execute("DELETE FROM PeerAdviser WHERE StudentNumber=?",(studentnumber,))

    def remove_admin(self, adminid):
        with self.db:
            self.cs.execute("DELETE FROM Admin WHERE AdminID=?",(adminid,))

    def remove_schedule(self, studentnumber):
        with self.db:
            self.cs.execute("DELETE FROM AdvisingSchedule WHERE StudentNumber=?",(studentnumber,))

    #Updates advisee details. Can only be accessed by an admin.
    def update_advisee(self, studentnumber, advisee):
        with self.db:
            self.cs.execute("UPDATE Advisee SET StudentNumber=?, FirstName=?, MiddleName=?, LastName=?, Program=?, ContactNumber=?, HomeAddress=?, EmailAddress=? WHERE StudentNumber=?", (advisee.studentnumber, advisee.firstname, advisee.middlename, advisee.lastname, advisee.program, advisee.contactnumber, advisee.homeaddress, advisee.emailaddress, studentnumber))

    #Updates peer adviser details. Can only be accessed by an admin.
    def update_peeradviser(self, studentnumber, peeradviser, dayone, timeone, daytwo, timetwo):
        accountid = str(peeradviser.studentnumber)
        with self.db:
            self.cs.execute("UPDATE PeerAdviser SET StudentNumber=?, FirstName=?, MiddleName=?, LastName=?, Program=?, ContactNumber=?, Organization=?, EmailAddress=? WHERE StudentNumber=?", (peeradviser.studentnumber, peeradviser.firstname, peeradviser.middlename, peeradviser.lastname, peeradviser.program, peeradviser.contactnumber, peeradviser.organization, peeradviser.emailaddress, studentnumber))
            self.cs.execute("UPDATE Login SET AccountID=? WHERE AccountID=?",(accountid, studentnumber))
            self.cs.execute("UPDATE AdvisingSchedule SET StudentNumber=?, DayOne=?, TimeOne=?, DayTwo=?, TimeTwo=? WHERE StudentNumber=?", (peeradviser.studentnumber, dayone, timeone, daytwo, timetwo, studentnumber))

    #Updates admin details. Can only be accessed by fellow admins.
    def update_admin(self, adminid, admin):
        with self.db:
            self.cs.execute("UPDATE Admin SET AdminID=?, FirstName=?, MiddleName=?, LastName=?, EmailAddress=? WHERE AdminID=?", (admin.adminid, admin.firstname, admin.middlename, admin.lastname, admin.emailaddress, adminid))
            self.cs.execute("UPDATE Login SET AccountID=? WHERE AccountID=?",(admin.adminid, adminid))

    def get_schedule(self, studentnumber):
        self.cs.execute("SELECT DayOne, TimeOne, DayTwo, TimeTwo from AdvisingSchedule WHERE StudentNumber=?",(studentnumber,))
        return self.cs.fetchone()

    def get_subjects(self, field):
        self.cs.execute("SELECT Code FROM Subject WHERE Field=?",(field,))
        return self.cs.fetchall()

    def get_subject(self, code):
        self.cs.execute("SELECT Title FROM Subject WHERE Code=?",(code,))
        return self.cs.fetchone()

    #Uses student number to get advisee information.
    def get_advisee(self, studentnumber):
        self.cs.execute("SELECT * FROM Advisee WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchone()

    #Uses student nubmer to get peer adviser information.
    def get_peeradviser(self, studentnumber):
        self.cs.execute("SELECT * FROM PeerAdviser WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchone()

    #Uses admin ID to get admin information
    def get_admin(self, adminid):
        self.cs.execute("SELECT * FROM Admin WHERE AdminID=?",(adminid,))
        return self.cs.fetchone()

    #Uses the account id to get the passsword
    def get_password(self, accountid):
        accountid = str(accountid)
        self.cs.execute("SELECT Password FROM Login WHERE AccountID=?", (accountid,))
        return self.cs.fetchone()

    def change_password(self, accountid, password):
        accountid = str(accountid)
        with self.db:
            self.cs.execute("UPDATE Login SET Password=? WHERE AccountID=?", (password, accountid))

    def delete_user(self, accountid):
        accountid = str(accountid)
        with self.db:
            self.cs.execute("DELETE FROM Login WHERE AccountID=?", (accountid,))

    #Logs the time and date of the start of an advisee's tutorial period
    def advisee_timein(self, studentnumber, subject, adviserid):
        date = datetime.datetime.now().strftime("%m-%d-%Y")
        timein = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("INSERT INTO SessionLog(StudentNumber, Subject, AdviserID, Date, TimeIn) VALUES(?,?,?,?,?)", (studentnumber, subject, adviserid, date, timein))

    #Logs the time of the end of an advisee's tutorial period
    def advisee_timeout(self, studentnumber, evaluation):
        timeout = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("UPDATE SessionLog SET TimeOut=?, Evaluation=? WHERE StudentNumber=? AND TimeOut IS NULL", (timeout, evaluation, studentnumber))

    #Logs the time in of a peer adviser
    def peeradviser_timein(self, studentnumber):
        date = datetime.datetime.now().strftime("%m-%d-%Y")
        timein = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("INSERT INTO TimeSheet(StudentNumber, Date, TimeIn) VALUES(?,?,?)", (studentnumber, date, timein))

    #Logs the time out of a peer adviser
    def peeradviser_timeout(self, studentnumber):
        timeout = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("UPDATE TimeSheet SET TimeOut=? WHERE StudentNumber=? AND TimeOut IS NULL", (timeout, studentnumber))

    #Returns the session log of an advisee
    def get_studentsessionlog(self, studentnumber):
        self.cs.execute("SELECT Date, TimeIn, TimeOut, Subject, AdviserID FROM SessionLog WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchall()

    #Returns the timesheet record of a peer adviser
    def get_studenttimesheet(self, studentnumber):
        self.cs.execute("SELECT Date, TimeIn, TimeOut FROM TimeSheet WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchall()

    #Returns the session log of an advisee
    def get_dailysessionlog(self, date):
        self.cs.execute("SELECT StudentNumber, TimeIn, TimeOut, Subject, AdviserID FROM SessionLog WHERE Date=?", (date,))
        return self.cs.fetchall()

    #Returns the timesheet record of a peer adviser
    def get_dailytimesheet(self, date):
        self.cs.execute("SELECT StudentNumber, TimeIn, TimeOut FROM TimeSheet WHERE Date=?", (date,))
        return self.cs.fetchall()

    #Returns a specific session identified by its log ID
    def get_session(self, logid):
        self.cs.execute("SELECT TimeIn, TimeOut, Subject, AdviserID FROM SessionLog WHERE LogID=?", (logid,))
        return self.cs.fetchone()

    #Returns a specific time log from the time sheet identified by its log ID
    def get_timelog(self, logid):
        self.cs.execute("SELECT TimeIn, TimeOut FROM SessionLog WHERE LogID=?", (logid,))
        return self.cs.fetchone()

    def get_emailadviser(self):
        self.cs.execute("SELECT EmailAddress FROM PeerAdviser")
        return self.cs.fetchall()
    
    def get_emailadvisee(self):
        self.cs.execute("SELECT EmailAddress FROM Advisee")
        return self.cs.fetchall()
    
    #Updates the session log, can only be used by an admin.
    def update_sessionlog(self, logid, timein, timeout, subject, adviserid):
        with self.db:
            self.cs.execute("UPDATE SessionLog SET TimeIn=?, TimeOut=?, Subject=?, AdviserID=? WHERE LogID=?", (timein, timeout, subject, adviserid, logid))

    #Updates the timesheet, can only be used by an admin.
    def update_timesheet(self, logid, timein, timeout):
        with self.db:
            self.cs.execute("UPDATE TimeSheet SET TimeIn=?, TimeOut=? WHERE LogID=?", (timein, timeout, logid))

    #Registers a user account
    def register_user(self, accountid, password):
        accountid = str(accountid)
        password = self.hash_password(password)
        with self.db:
            self.cs.execute("INSERT INTO Login VALUES(?,?)", (accountid, password))

    #Hash the password. Reference: https://www.pythoncentral.io/hashing-strings-with-python/
    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + 'g' + salt

    #Check if student number is in advisee record
    def in_advisee(self, studentnumber):
        self.cs.execute("SELECT count(*) FROM Advisee WHERE StudentNumber=?",(studentnumber,))
        count, = self.cs.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Check if student number is in peer adviser record
    def in_peeradviser(self, studentnumber):
        self.cs.execute("SELECT count(*) FROM PeerAdviser WHERE StudentNumber=?",(studentnumber,))
        count, = self.cs.fetchone()
        if count != 0:
            return True
        else:
            return False

    #Check if adminid is in admin record
    def in_admin(self, adminid):
        self.cs.execute("SELECT count(*) FROM Admin WHERE AdminID=?",(adminid,))
        count, = self.cs.fetchone()
        if count != 0:
            return True
        else:
            return False

    def terminate_nulls(self):
        with self.db:
            self.cs.execute("UPDATE TimeSheet SET TimeOut=? WHERE TimeOut IS NULL",(placeholder,))
            self.cs.execute("UPDATE SessionLog SET TimeOut=? WHERE TimeOut IS NULL",(placeholder,))

    def close(self):
        self.db.close()
        