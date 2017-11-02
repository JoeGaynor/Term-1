""""
Password checker, forbids certain words being a password, double entry confirmation, length check
"""""
import string, random

__author__ = "Joseph Gaynor"
__email__ = "U1753547@hud.ac.uk"
__date__ = "2017/10/26"

banned_passwords = ["Password", "password", "sesame", "Sesame", "Letmein", "LetMeIn", "Qwerty", "Cheese"]
character_list = []
for i in range(128):
    character_list.append(chr(i))
new_password = []
for x in range(random.randint(6, 12)):
    new_password.append(character_list(random.randint(0, 128)))

print(f"your new password is: {new_password}")

while 1:
    password1 = input("PLease enter your new password: ")
    password2 = input("Please confirm the new password: ")

    if password1 == password2:
        if 12 >= len(password1) >= 6:
            if password1 in banned_passwords:
                print("Invalid password, please change")
            else:
                print("Password changed")
                break
        else:
            print("Incorrect character number, must be between 6 and 12 characters")
    else:
        print("password confirmation does not match")
