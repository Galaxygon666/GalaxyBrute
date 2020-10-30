import hashlib
import time
import pyfiglet

def main():
    print(pyfiglet.figlet_format("GalaxyBrute"))
    input_pass = input("Insert md5 encrypted password: \n")
    with open("wordlist.txt", encoding="utf-8") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    start_time = time.time()
    print("\n\n" + "-"*14 + "GalaxyBrute" + "-"*14 + "\n")
    print("Password: " + cracker(content, input_pass) + "\n")
    print("--- in %s seconds ---" % (time.time() - start_time))


def cracker(content, input):
    for ele in content:
        temp_pass = hashlib.md5(ele.encode())
        pass_guess = str(temp_pass.hexdigest())
        #print(pass_guess)
        if str(pass_guess) == str(input):
            return ele
            break

if __name__ == '__main__':
    main()
