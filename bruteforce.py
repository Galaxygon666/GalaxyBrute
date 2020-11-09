import sys
import hashlib
import time
import pyfiglet
from printy import printy
from os import system, name

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    cuda_bool = False

    printy(pyfiglet.figlet_format("GalaxyBrute"), "b")
    print("!NO SALTED HASHES!")
    input_gpu = input("Do you have an nvidea gpu with cuda? (y/n) \n")
    if(input_gpu == "y"):
        cuda_bool = True
        clear()
    elif(input_gpu == "n"):
        cuda_bool = False
        clear()
    else:
        print("Invalid input!")
        sys.exit(1)

    printy(pyfiglet.figlet_format("GalaxyBrute"), "b")
    input_method = input("Choose hashing algorithm:\n" +
    "1. MD5\n" +
    "2. SHA-1\n" +
    "3. SHA-224\n" +
    "4. SHA-256\n" +
    "5. SHA-384\n" +
    "6. SHA-512\n" +
    ">")

    input_pass = input("Insert encrypted password: \n>")
    input_wordlist = input("Input path to wordlist: \n>")
    wordlister(input_wordlist, input_pass, int(input_method))


def wordlister(wordlist, password, method):
    pass_test = []
    with open(wordlist, "r", encoding="ISO-8859-1") as f:
        content = f.readlines()

    for line in content:
        pass_test.append(line.strip())


    if method == 1:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        md5(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    elif method == 2:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        sha1(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    elif method == 3:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        sha224(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    elif method == 4:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        sha256(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    elif method == 5:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        sha384(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    elif method == 6:
        start_time = time.time()
        print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
        sha512(pass_test, password)
        print("------ %s seconds ------" % (time.time() - start_time))

    else:
        print("Somn went wrong boss")

def md5(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.md5(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")


def sha1(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.sha1(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")


def sha224(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.sha224(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")


def sha256(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.sha256(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")


def sha384(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.sha384(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")


def sha512(wordlist, input):
    for ele in wordlist:
        print("Trying: " + ele)
        temp_pass = hashlib.sha512(ele.encode())
        pass_guess = str(temp_pass.hexdigest())

        if str(pass_guess) == str(input):
            print("\n\n" + "-"*14 + "Password found!" + "-"*14 + "\n")
            print("Password: " + ele + "\n")
            print("-" * 43 + "\n")
            return 0
            break

    print("\n\n" + "-"*14 + "Password not found!" + "-"*14 + "\n")



if __name__ == '__main__':
    main()
