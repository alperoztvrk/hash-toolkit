import hashlib
from termcolor import colored

enterCharacter = input("Enter String: ")
print(colored("<<<<<<<MD5>>>>>>>", 'yellow'))

hashjob = hashlib.md5()
hashjob.update (enterCharacter.encode())
print(colored(hashjob.hexdigest(), 'green'))

print(colored("<<<<<<<Sha1>>>>>>>", 'yellow'))

hashjob = hashlib.sha1()
hashjob.update (enterCharacter.encode())
print(colored(hashjob.hexdigest(), 'green'))

print(colored("<<<<<<<Sha256>>>>>", 'yellow'))

hashjob = hashlib.sha256()
hashjob.update (enterCharacter.encode())
print(colored(hashjob.hexdigest(), 'green'))

print(colored("<<<<<<<512>>>>>>>", 'yellow'))

hashjob = hashlib.sha512()
hashjob.update (enterCharacter.encode())
print(colored(hashjob.hexdigest(), 'green'))