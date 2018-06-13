#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 12/6/2018 2:37 PM
# @Author  : FaccordX
# @File    : login.py

ofile1 = open("loginlist.txt","r")
ofile2 = open("lockeduser.txt", "r+")
listsaved = []
listlocked = []
while 1:
    line = ofile1.readline()
    if not line:
        break
    else:
        listsaved.append(line.replace("\n", ""))
ofile1.close()
while 1:
    line2 = ofile2.readline()
    if not line2:
        break
    else:
        listlocked.append(line2)
print("welcome to join the login interface!")
for i in range(3):
    print("so we start to login")
    username = input("Username: ")
    password = input("password: ")
    if username in listlocked:
        print("this user locked.")
        break
    elif not any(username in x for x in listsaved):
        print("you haven't registered yet.")
        break
    else:
        if username + " " + password in listsaved:
            print("login successful")
            break
        else:
            print("login wrongly")
        if i == 2:
            ofile2.seek(0)
            ofile2.truncate(0)
            ofile2.write(username)
            ofile2.close()
            print("you had tried 3 time already, the user have locked.")
