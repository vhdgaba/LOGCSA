import sqlite3, datetime

class FileHandler:
    def __init__(self, database):
        self.db = sqlite3.connect(database)
        self.cs = self.db.cursor()

    def add_advisee(self, advisee):
        with self.db:
            self.cs.execute("INSERT INTO Advisee VALUES(?,?,?,?,?,?,?)", (advisee.studentnumber, advisee.firstname, advisee.middlename, advisee.lastname, advisee.program, advisee.contactnumber, advisee.homeaddress))

    def add_peeradviser(self, peeradviser):
        with self.db:
            self.cs.execute("INSERT INTO PeerAdviser VALUES(?,?,?,?,?,?,?)", (peeradviser.studentnumber, peeradviser.firstname, peeradviser.middlename, peeradviser.lastname, peeradviser.program, peeradviser.contactnumber, peeradviser.organization))

    #Updates advisee details. Can only be accessed by an admin.
    def update_advisee(self, studentnumber, advisee):
        with self.db:
            self.cs.execute("UPDATE Advisee SET StudentNumber=?, FirstName=?, MiddleName=?, LastName=?, Program=?, ContactNumber=?, HomeAddress=? WHERE StudentNumber=?", (advisee.studentnumber, advisee.firstname, advisee.middlename, advisee.lastname, advisee.program, advisee.contactnumber, advisee.homeaddress, studentnumber))

    #Updates peer adviser details. Can only be accessed by an admin.
    def update_peeradviser(self, studentnumber, peeradviser):
        with self.db:
            self.cs.execute("UPDATE PeerAdviser SET StudentNumber=?, FirstName=?, MiddleName=?, LastName=?, Program=?, ContactNumber=?, Organization=? WHERE StudentNumber=?", (peeradviser.studentnumber, peeradviser.firstname, peeradviser.middlename, peeradviser.lastname, peeradviser.program, peeradviser.contactnumber, peeradviser.organization, studentnumber))

    #Uses student number to get advisee information.
    def get_advisee(self, studentnumber):
        self.cs.execute("SELECT * FROM Advisee WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchone()

    #Uses student nubmer to get peer adviser information.
    def get_peeradviser(self, studentnumber):
        self.cs.execute("SELECT * FROM PeerAdviser WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchone()

    #Logs the time and date of the start of an advisee's session.
    def start_session(self, studentnumber, subject, adviser):
        date = datetime.datetime.now().strftime("%m-%d-%Y")
        timein = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("INSERT INTO SessionLog(StudentNumber, Subject, Adviser, Date, TimeIn) VALUES(?,?,?,?,?)", (studentnumber, subject, adviser, date, timein))

    #Logs the time of the end of an advisee's session.
    def end_session(self, studentnumber):
        timeout = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("UPDATE SessionLog SET TimeOut=? WHERE StudentNumber=? AND TimeOut IS NULL", (timeout, studentnumber))

    #Logs the time in of a peer adviser
    def time_in(self, studentnumber):
        date = datetime.datetime.now().strftime("%m-%d-%Y")
        timein = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("INSERT INTO TimeSheet(StudentNumber, Date, TimeIn) VALUES(?,?,?)", (studentnumber, date, timein))

    #Logs the time out of a peer adviser
    def time_out(self, studentnumber):
        timeout = datetime.datetime.now().strftime("%H:%M")
        with self.db:
            self.cs.execute("UPDATE TimeSheet SET TimeOut=? WHERE StudentNumber=? AND TimeOut IS NULL", (timeout, studentnumber))

    #Returns the session log of an advisee
    def get_sessionlog(self, studentnumber):
        self.cs.execute("SELECT * FROM SessionLog WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchall()

    #Returns the timesheet record of a peer adviser
    def get_timesheet(self, studentnumber):
        self.cs.execute("SELECT * FROM TimeSheet WHERE StudentNumber=?", (studentnumber,))
        return self.cs.fetchall()

    #Updates the session log, can only be used by an admin.
    def update_sessionlog(self, studentnumber, timein, timeout, subject, adviserid):
        with self.db:
            self.cs.execute("UPDATE SessionLog SET TimeIn=?, TimeOut=?, Subject=?, AdviserID=? WHERE StudentNumber=?", (timein, timeout, subject, adviserid, studentnumber))

    #Updates the timesheet, can only be used by an admin.
    def update_timesheet(self, studentnumber, timein, timeout):
        with self.db:
            self.cs.execute("UPDATE TimeSheet SET TimeIn=?, TimeOut=? WHERE StudentNumber=?", (timein, timeout, studentnumber))

    def close(self):
        self.db.close()