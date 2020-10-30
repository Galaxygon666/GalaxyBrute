import random
import string

chars = string.ascii_letters + string.punctuation  + string.digits

number = input("Number of passwords: ")
number = int(number)

lenght = input("Lenght of passwords: ")
lenght = int(lenght)

passwords = []

for p in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)

    passwords.append(password)

f = open("wordlist.txt", "w+")
for element in passwords:
    f.write(element + "\n")
