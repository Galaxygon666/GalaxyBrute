import hashlib
import time
import pyfiglet

def main():
    print(pyfiglet.figlet_format("GalaxyBrute"))
    input_pass = input("Insert md5 encrypted password: \n")
    input_wordlist = input("Input path to wordlist: \n")
    with open(input_wordlist, "r", encoding="ISO-8859-1") as f:
        content = f.readlines()

    wordlist_list = []

    for line in content:
        wordlist_list.append(line.strip())


    start_time = time.time()
    print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
    cracker(wordlist_list, input_pass)
    print("------ %s seconds ------" % (time.time() - start_time))

def cracker(wordlist, input):
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

if __name__ == '__main__':
    main()
