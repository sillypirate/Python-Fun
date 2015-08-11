#!/usr/bin/env python

###########################
#Grep.py                  #
#Team Project 1           #
#@author Matthew Collins  #
#@author Eric Smith       #
###########################

import glob
import sys

def grep(*args): #"""Performs the Grep Command"""
    argCount = len(args)
    if argCount == 2:
        if args[1] == "*":
            for file in glob.glob("*.txt"): #"""Checks the current directory for a new file"""
                for line in open(file): #"""Checks a line of the file and prints if it contains the search"""
                    if args[0] in line.strip():
                        print(file, ":", line, end=""),
        else:
            for line in open(args[1]): #"""Checks a line of the file and prints if it contains ths search"""
                if args[0] in line.strip():
                    print(args[1], ":", line, end=""),
    else:
        if args[0] == "-v":
            if args[2] == "*":
                for file in glob.glob("*.txt"): #"""Checks the current directory for a new file"""
                    for line in open(file): #"""Checks a line of the file and prints if does NOT contain the search"""
                        if args[1] not in line.strip():
                            print(file, ":", line, end=""),
            else:
                currNum = 2
                while currNum <= (argCount-1): #"""Increases currNum by 1 """
                    for line in open(args[currNum]): #"""Checks a line of the file and prints if does NOT contain
                                                     #  the search"""
                        if args[1] not in line.strip():
                            print(args[currNum], ":", line, end=""),
                    currNum = currNum+1
        elif args[0] == "-x":
            if args[2] == "*":
                for file in glob.glob("*.txt"): #"""Checks the current directory for a new file"""
                    for line in open(file): #"""Checks a line of the file and prints if finds exact search"""
                        if args[1] == line.strip():
                            print(file, ":", line, end=""),
            else:
                currNum = 2
                while currNum <= (argCount-1): #"""Increases currNum by 1 """
                    for line in open(args[currNum]): #"""Checks a line of the file and prints if finds exact search"""
                        if args[1] == line.strip():
                            print(args[currNum], ":", line, end=""),
                    currNum = currNum+1
        else:
            currNum = 1
            while currNum <= (argCount-1): #"""Increases currNum by 1 """
                for line in open(args[currNum]): #"""Checks a line of the file and prints if it finds the search"""
                    if args[0] in line.strip():
                        print(args[currNum], ":", line, end=""),
                currNum = currNum+1

if __name__ == '__main__':
    grep(sys.argv)