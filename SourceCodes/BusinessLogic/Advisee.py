from DataAccess.FileHandler import FileHandler
from BusinessLogic.Student import Student

userfh = FileHandler('../Data/record.db')
defaultsubjecttitle = 'General Information'

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

if __name__ == '__main__':
    pass