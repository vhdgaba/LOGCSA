#COE125/C1 - MU-CYCU
#Gaba, Vince Harley
#Manuel, Lester
#He, Zhiyang

from Data.FileHandler import FileHandler
from Objects.Student import Advisee, PeerAdviser

#fh = FileHandler('tutorialon.db')
#fh.cs.execute('CREATE TABLE Login(AccountID integer primary key, Password text)')
#fh.cs.execute('CREATE TABLE Admin(AdminID integer primary key, FirstName text, MiddleName text, LastName text)')
#fh.cs.execute('CREATE TABLE Advisee(StudentNumber integer primary key, FirstName text, MiddleName text, LastName text, Program text, ContactNumber text, HomeAddress text )')
#fh.cs.execute('CREATE TABLE PeerAdviser(StudentNumber integer primary key, FirstName text, MiddleName text, LastName text, Program text, ContactNumber text, Organization text)')
#fh.cs.execute('CREATE TABLE SessionLog(LogID integer primary key autoincrement, StudentNumber integer, Date text, TimeIn text, TimeOut text, Subject text, AdviserID integer)')
#fh.cs.execute('CREATE TABLE TimeSheet(LogID integer primary key autoincrement, StudentNumber integer, Date text, TimeIn text, TimeOut text)')
#fh.close()