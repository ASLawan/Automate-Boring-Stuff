#!/usr/bin/python3
import getpass
#valid password check
# min length 10
# Must start with a capital letter
# Must contain at leats 1 lowercase letter
# Must contain at least 1 integer
# Must contain one special characater
# Must not contain space character

def password_check(pwd):
    lflag = 0
    uflag = 0
    sflag = 0
    iflag = 0
    xflag = 0
    ssflag = 0

    length = len(pwd)
    if length > 10:
        lflag = 1
    for i in range(length):
        if pwd[0].isalpha() and pwd[0].isupper():
            uflag = 1
        if pwd[i].islower():
            sflag = 1
        if pwd[i].isdecimal():
            iflag = 1
        if pwd[i] in ['@', '#', '$', '&']:
            xflag = 1
        if not pwd[i].isspace():
            ssflag = 1 

    if uflag == 1 and lflag == 1 and iflag == 1 and sflag == 1 and ssflag == 1 and xflag == 1:
        return True
    else:
        return False


def main():
    trials = 3
    i = 0
    while i < trials:
        print("Please create your account password: ")
        pwd = getpass.getpass("Enter password here: ")
        password = password_check(pwd)

        if password:
            cpwd = getpass.getpass("Confirm your password: ")
            if pwd == cpwd:
                new_pwd = []
                for i in range(len(pwd)):
                    if i == 0:
                        new_pwd.append(pwd[i])
                    else:
                        new_pwd.append('*')
                print("Your password is valid: {}".format("".join(new_pwd)))
            else:
                print("The two passwords do not match!")
        else:
            print("A valid password must:")
            print("* Be at least 10 characters long")
            print("* Start with an uppercase letter")
            print("* Have at least a lowercase letter")
            print("* Have at least 1 integer")
            print("* Have at least 1 special character")
            print("* Must not have whitespace")

        i += 1
    
    return "Try again later!"
        

main()
