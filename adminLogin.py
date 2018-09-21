from getPass import getPass
from fileHandling import fileHandling
from formatString import changeFormat
from search import search

buffer = []
usernames = []
passwords = []
reader = fileHandling()
reader.ReadFile(buffer,passwords)   
 
for un in buffer:
    usernames.append(changeFormat(un))

while True:
    username = input('Username: ')
    password = getpass('Password: ')

    username = changeFormat(username)

    index = search.search(username,usernames)
    
    if index != None:
        if passwords[index] == password:
            print('Login success!')
            break
        else:
            print('Wrong password!')
            input()
    else:
        print('Username not found.')
        input()
