#COE125/C1 - MU-CYCU
#Gaba, Vince Harley
#Manuel, Lester
#He, Zhiyang

from BusinessLogic.Session import Session
from BusinessLogic.User import Admin, Advisee, PeerAdviser
from getpass import getpass

ses = Session()

def menu():
    print('Commands:\nLOGIN <usertype>\tLog in as ADMIN, ADVISEE, or PEERADVISER\nLOGOUT <usertype>\tLog out an ADVISEE or a PEERADVISER that is currently in session\nREGISTER\tSign up an advisee account\nSHOW <studenttype>\tDisplay ALL the users, the ADVISEES, or the PEERADVISERS present in the current session.\nHELP\tSee the list of all available commands.\nEXIT\tTerminate the session and exit the program.\n'.expandtabs(25))

def register():
    print('Registration: ')
    studentnumber = input('Student Number [10-digit]: ')
    firstname = input('First Name: ')
    middlename = input('Middle Name: ')
    lastname = input('Last Name: ')
    program = input('Program: ')
    contactnumber = input('Contact Number: ')
    address = input('Address: ')
    if ses.register_advisee(studentnumber, firstname, middlename, lastname, program, contactnumber, address):
        print('Registration Success!\n')
    else:
        print(ses.errormsg + '\n')

def select_subject():
    subjectids = []
    titles = []
    print('Available Subjects:')
    for i, subject in enumerate(ses.get_subjects()):
        subjectids.append(subject[0])
        titles.append(subject[1])
        print('{}\t{}'.format(subjectids[i], titles[i]).expandtabs(5))
    choice = int(input('Select a subject ID: '))
    if choice in subjectids:
        subject, = ses.get_subject(choice)
        print('Subject chosen: ' + subject + '\n')
        return subject
    else:
        while choice not in subjectids:
            print("Please select only from the available choices.")
            choice = int(input('Select a subject ID: '))
            if choice in subjectids:
                subject, = ses.get_subject(choice)
                print('Subject chosen: ' + subject + '\n')
                return subject
            
def select_adviser():
    adviserids = []
    names = []
    print('Available Peer Advisers:')
    for adviser in ses.peeradvisers:
        adviserids.append(adviser.studentnumber)
        names.append(str(adviser))
        print('  [{}] : {}, {} {}.'.format(adviser.studentnumber, adviser.lastname, adviser.firstname, adviser.middlename[:1]))
    choice = int(input('Select adviser ID: '))
    if choice in adviserids:
        adviser = ses.peeradvisers[adviserids.index(choice)]
        print('Adviser chosen: ' + str(adviser))
        return adviser.studentnumber
    else:
        while choice not in adviserids: 
            print("Please select only from the available choices.")
            choice = int(input('Select adviser ID: '))
            if choice in adviserids:
                adviser = ses.peeradvisers[adviserids.index(choice)]
                print('Subject chosen: ' + str(adviser))
                return adviser.studentnumber

def show(arg):
    if arg == 'all':
        print('Peer Advisers: ', end = '')
        if ses.peeradvisercount != 0:
            print('{} in session'.format(ses.peeradvisercount))
            for adviser in ses.peeradvisers:
                print('  [{}] : {}, {} {}.'.format(adviser.studentnumber, adviser.lastname, adviser.firstname, adviser.middlename[:1]))
        else:
            print('No peer advisers in session.')
        print()
        print('Advisees: ', end = '')
        if ses.adviseecount != 0:
            print('{} in session'.format(ses.adviseecount))
            for advisee in ses.advisees:
                print('  [{}] {}, {} {}.'.format(advisee.studentnumber, advisee.lastname, advisee.firstname, advisee.middlename[:1]))
        else:
            print('No advisees in session.')
        print()
    elif arg == 'advisees':
        print('Advisees: ', end = '')
        if ses.adviseecount != 0:
            print('{} in session'.format(ses.adviseecount))
            for advisee in ses.advisees:
                print('  [{}] : {}, {} {}.'.format(advisee.studentnumber, advisee.lastname, advisee.firstname, advisee.middlename[:1]))
        else:
            print('No advisees in session.')
        print()
    elif arg == 'peeradvisers':
        print('Peer Advisers: ', end = '')
        if ses.peeradvisercount != 0:
            print('{} in session'.format(ses.peeradvisercount))
            for adviser in ses.peeradvisers:
                print('  [{}] : {}, {} {}.'.format(adviser.studentnumber, adviser.lastname, adviser.firstname, adviser.middlename[:1]))
        else:
            print('No peer advisers in session.')
        print()
    elif arg == '?':
        print('Command: SHOW <studenttype>\nALL\tDisplays the list of all advisees and peer advisers that are currently in session.\nADVISEES\tDisplays the list of all advisees that are currently in session.\nPEERADVISERS\tDisplays the list of all peer advisers that are currently in session.\n'.expandtabs(20))
    else:
        print('Invalid argument for <studenttype>\nUse \'SHOW ?\' to see a list of valid arguments.\n')

def login(arg):
    if arg == 'admin':
        pass
    elif arg == 'peeradviser':
        studentnumber = input('Student Number: ')
        password = getpass('Password: ')
        if ses.login_peeradviser(studentnumber, password):
            PeerAdviser(*ses.get_peeradviser(studentnumber)).time_in()
            print('Login success!\n')
        else:
            print(ses.errormsg + '\n')
    elif arg == 'advisee':
        studentnumber = input('Student Number: ')
        if ses.login_advisee(studentnumber):
            subject = select_subject()
            adviser = select_adviser()
            Advisee(*ses.get_advisee(studentnumber)).time_in(subject, adviser)
            print('Login success!\n')
        else:
            print(ses.errormsg + '\n')
    elif arg == '?':
        print('Command: LOGIN <usertype>\nADMIN\tLog in with an admin account, gaining admin privileges.\nADVISEE\tLog in as an advisee, will be prompted to choose a subject and a peer adviser for the tutoring session.\nPEERADVISER\tLog in as a peer adviser, being included in the list which the advisees can choose from.\n'.expandtabs(20))
    else:
        print('Invalid argument for <usertype>\nUse \'LOGIN ?\' to see a list of valid arguments.\n')
    
def logout(arg):
    if arg == 'peeradviser':
        studentnumber = input('Student Number: ')
        if ses.logout_peeradviser(studentnumber):
            PeerAdviser(*ses.get_peeradviser(studentnumber)).time_out()
            print('Logout success!\n')
        else:
            print(ses.errormsg + '\n')
    elif arg == 'advisee':
        studentnumber = input('Student Number: ')
        if ses.logout_advisee(studentnumber):
            Advisee(*ses.get_advisee(studentnumber)).time_out()
            print('Logout success!\n')
        else:
            print(ses.errormsg + '\n')
    elif arg == '?':
        print('Command: LOGOUT <usertype>\nADVISEE\tLog out an advisee and record the time out in the session log.\nPEERADVISER\tLog out a peer adviser and record the time out in the timesheet.\n'.expandtabs(20))
    else:
        print('Invalid argument for <usertype>\nUse \'LOGOUT ?\' to see a list of valid arguments.\n')
         
        
    
def start():
    stop = False
    control = 'Session'
    print('Session started.\n')
    menu()
    while not stop:
        
        inp = input('(TutorialOn) {}>>'.format(control)).strip().lower().split(' ')
        
        if inp[0] == 'exit':
            stop = True
            pass
        
        elif inp[0] == '':
            pass
        
        elif inp[0] == 'login':
            if len(inp) == 1:
                print('Missing arguments: <usertype>\nUse \'LOGIN ?\' to see a list of valid arguments.\n')
            elif len(inp) == 2:
                login(inp[1])
            else:
                print('Invalid argument for <usertype>\nUse \'LOGIN ?\' to see a list of valid arguments.\n')
            
        elif inp[0] == 'logout':
            if len(inp) == 1:
                print('Missing arguments: <usertype>\nUse \'LOGOUT ?\' to see a list of valid arguments.\n')
            elif len(inp) == 2:
                logout(inp[1])
            else:
                print('Invalid argument for <usertype>\nUse \'LOGOUT ?\' to see a list of valid arguments.\n')
            
        elif inp[0] == 'show':
            if len(inp) == 1:
                print('Missing arguments: <studenttype>\nUse \'SHOW ?\' to see a list of valid arguments.\n')
            elif len(inp) == 2:
                show(inp[1])
            else:
                print('Invalid argument for <studenttype>\nUse \'SHOW ?\' to see a list of valid arguments.\n')
            
        elif inp[0] == 'register':
            register()
            
        elif inp[0] == 'help' or inp[0] == '?':
            menu()
            
        else:
            print('\'{}\' is not a recognized command.\nUse \'HELP\' to see a complete list of available commands.\n'.format(inp[0]))
    print('Session ended.')
    
if __name__ == '__main__':
    start()