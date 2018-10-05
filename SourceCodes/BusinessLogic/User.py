from DataAccess.FileHandler import FileHandler

userfh = FileHandler('../Data/record.db')
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

if __name__ == '__main__':
    pass