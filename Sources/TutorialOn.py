#COE125/C1 - MU-CYCU
#Gaba, Vince Harley
#Manuel, Lester
#He, Zhiyang

from Session import Session
from User import Admin, Advisee, PeerAdviser

ses = Session()

def menu():
    print('1 - Advisee Login\n2 - Peer Adviser Login\n3 - Admin Login\n4 - Show Online\n')

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
        pass
    elif arg == 'advisee':
        studentnumber = input('Student Number: ')
        if ses.login_advisee(studentnumber):
            print('Login success!\n')
        else:
            print(ses.errormsg + '\n')
    elif arg == '?':
        print('Command: LOGIN <usertype>\nADMIN\tLog in with an admin account, gaining admin privileges.\nADVISEE\tLog in as an advisee, will be prompted to choose a subject and a peer adviser for the tutoring session.\nPEERADVISER\tLog in as a peer adviser, being included in the list which the advisees can choose from.\n'.expandtabs(20))
    else:
        print('Invalid argument for <usertype>\nUse \'LOGIN ?\' to see a list of valid arguments.\n')
    
def start():
    stop = False
    control = 'Session'
    print('Session started.')
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
            
        elif inp[0] == 'show':
            if len(inp) == 1:
                print('Missing arguments: <studenttype>\nUse \'SHOW ?\' to see a list of valid arguments.\n')
            elif len(inp) == 2:
                show(inp[1])
            else:
                print('Invalid argument for <studenttype>\nUse \'SHOW ?\' to see a list of valid arguments.\n')
            
        elif inp[0] == 'register':
            pass
            
        elif inp[0] == 'help' or inp[0] == '?':
            menu()
            
        else:
            print('\'{}\' is not a recognized input.\nUse \'HELP\' to see a complete list of commands.\n'.format(inp[0]))
            
if __name__ == '__main__':
    start()