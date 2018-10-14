from DataAccess.FileHandler import FileHandler
from BusinessLogic.Student import Student

userfh = FileHandler('../Data/record.db')
defaultsubjecttitle = 'General Information'

class PeerAdviser(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, organization, emailaddress):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber, emailaddress)
        self.organization = organization

    def time_in(self):
        userfh.peeradviser_timein(self.studentnumber)

    def time_out(self):
        userfh.peeradviser_timeout(self.studentnumber)

    def get_schedule(self):
        dayone, timeone, daytwo, timetwo = userfh.get_schedule(self.studentnumber)
        scheduleone = "{} {}".format(dayone,timeone)
        scheduletwo = "{} {}".format(daytwo, timetwo)
        return [scheduleone, scheduletwo]
    
if __name__ == '__main__':
    pass