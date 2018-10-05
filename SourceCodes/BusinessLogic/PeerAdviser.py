from DataAccess.FileHandler import FileHandler
from BusinessLogic.Student import Student

userfh = FileHandler('../Data/record.db')
defaultsubjecttitle = 'General Information'

class PeerAdviser(Student):
    def __init__(self,  studentnumber, firstname, middlename, lastname, program, contactnumber, organization):
        Student.__init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber)
        self.organization = organization

    def time_in(self):
        userfh.peeradviser_timein(self.studentnumber)

    def time_out(self):
        userfh.peeradviser_timeout(self.studentnumber)

if __name__ == '__main__':
    pass