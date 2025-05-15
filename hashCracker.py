#!/usr/bin/env python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
    try:
        with open(wordlist, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(colored("File not found. Please check the path and try again.", "red"))
        exit()

enterHash = input("Enter target hash: ")
wordList = input("Enter Wordlist Path: ")

pass_file = tryOpen(wordList)

for word in pass_file: 
    print(colored("[?Trying: "+ word.strip("\n"),'yellow'))
    enc_word = word.encode("latin-1")
    md5Digest = hashlib.md5(enc_word.strip()).hexdigest()
    if md5Digest == enterHash:
        print(colored("[+] Password Found: " + word.strip("\n"), "green"))
        exit()

print(colored("[!!] Password not found in the wordlist.", "red"))
