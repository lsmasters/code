# -*- coding: utf-8 -*-
"""
secure is a program to demonstrate simple and complex encryption methods
Created on Thu May  9 15:16:12 2019

@author: Larry Masters
"""
import os
import time


# method to display the menu and return the selection
def menu():
    print("Encryption Methods")
    print("1.  Shift encryption")
    print("2.  Substitution encryption")
    print("3.  xxxxxxxxxxxx encryption")
    print("4.  yyyyyyyyyyyy encryption")
    print("5.  zzzzzzzzzzzz encryption")
    answer = False
    while answer == False:
        meth = int(input("Select a number(1-5):  "))
        if meth > 0 and meth <= 5:
            answer = True
    return meth


# get the shift number
def getShift():
    done = False
    while not done:
        sh = int(input('Enter a shift key (1-25):  '))
        if sh > 0 and sh <= 25:
            done = True
    return sh


# simple SHIFT encription with a shift of 3
def shift(text):
    shNum = getShift()
    encode = ""
    for n in range(len(text)):
        num = ord(text[n])
        encode = encode + chr(num + shNum)
    return encode


def unShift(text):
    shNum = getShift()
    encode = ""
    for n in range(len(text)):
        num = ord(text[n])
        encode = encode + chr(num - shNum)
    return encode


def subs(text):
    # serveral different keys can be chosen with input number
    key = 'CDEABRSTUVWXFGHIJYZKLMNOPQR'
    uText = text.upper()
    encode = ""
    for n in range(len(uText)):
        num = ord(uText[n])
        if num > 64 and num <= 90:
            encode = encode + key[num - 65]
        else:
            encode = encode + uText[n]
    return encode


def unSubs(text):
    # serveral different keys can be chosen with input number
    key = 'CDEABRSTUVWXFGHIJYZKLMNOPQ'
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encode = ""
    for n in range(len(text)):
        num = key.find(text[n])
        if num >= 0 and num <= 26:
            encode = encode + alp[num]
        else:
            encode = encode + text[n]
    return encode


# method = menu()

# get input string from user
i = input("Enter the text to encode and then <return>:  ")
# get encoded input
enc = shift(i)
print("The shift encriptions of \n", i, "\n is\n", enc)
# get decoded output
dec = unShift(enc)
print("and the decription is \n", dec)
enc = subs(i)
print("substituted text is \n", enc)
dec = unSubs(enc)
print("and the decription is \n", dec)
# keep output on monitor for a few seconds
time.sleep(1)
exit(0)