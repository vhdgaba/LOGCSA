class Student:
    def __init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
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