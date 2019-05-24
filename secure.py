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
    print("\n\nEncryption Methods")
    print("1.  SHIFT encryption")
    print("2.  SUBSTITUTION encryption")
    print("3.  xxxxxxxxxxxx encryption")
    print("4.  yyyyyyyyyyyy encryption")
    print("5.  QUIT")
    answer = False
    while answer == False:
        meth = int(input("Select a number(1-5):  "))
        if meth > 0 and meth <= 5 and meth == int(meth):
            answer = True
    return meth


# get the shift number
def getShift26():
    done = False
    while not done:
        sh = int(input('Enter a shift key (1-25):  '))
        if type(sh) not in [int]:
            raise TypeError("The shift must be an integer between 1 and 25 inclusive")
        if sh > 0 and sh <= 25:
            done = True
        else:
            raise ValueError("The number must be from 1 to 25")
    return sh


# simple SHIFT encription with a shift of 3
def shift(text,sh):
    encode = ""
    for n in range(len(text)):
        num = ord(text[n])
        encode = encode + chr(num + sh)
    return encode


def unShift(text,sh):
    encode = ""
    for n in range(len(text)):
        num = ord(text[n])
        encode = encode + chr(num - sh)
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

if __name__ == '__main__':
    q = False
    while q == False:
        method = int(menu())
        #check for exit
        if method == 5:
            break
        if method ==1 or method == 2:
            # get input string from user
            i = input("Enter the text to encode and then <return>:  ")
        if method == 1:
            #get shift number
            s = getShift26()
            # print encoded input
            en = shift(i, s)
            print("The shift encriptions of \n", i, "\n is\n", en)
            # print decoded output
            dec = unShift(en, s)
            print("\nand the decription is \n", dec)
        elif method == 2:
            #print encoded substitution text
            print("substituted text is \n", subs(i))
            #print decoded substitution text
            print("and the decription is \n", unSubs(subs(i)))
        elif method == 3:
            print ("\nThis method is not currently implemented.")
        elif method == 4:
            print("\nThis method is not currently implemented.")
        else:
            q = True
    exit(0)
