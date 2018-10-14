from BusinessLogic.User import User

class Student(User):
    def __init__(self, studentnumber, firstname, middlename, lastname, program, contactnumber, emailaddress):
        User.__init__(self, firstname, middlename, lastname, emailaddress)
        self.studentnumber = studentnumber
        self.program = program
        self.contactnumber = contactnumber

    def __eq__(self, other):
        try:
            return self.studentnumber == other.studentnumber
        except:
            return False

if __name__ == '__main__':
    pass