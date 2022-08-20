import random
import time
import string
import lists

minimum = 2
maximum = 5
pause = 2.5

string.punctuation += " "


def get_length(a, b):
    print("Welcome to the Secure Passphrase Generator.")
    time.sleep(pause)
    print("I will make a secure but memorable password from randomly selected words.")
    time.sleep(pause)
    length = input("Please enter your desired password length in words. "
                   "This should be a number between %d and %d.\n" % (a, b))
    while not length.isdigit() or (int(length) < a or int(length) > b):
        length = input("That is not a number between 2 and 5. Please try again.\n")
    return int(length)


def get_special():
    special = input("Please enter a special character to use between the words for added complexity. You may enter "
                    "either a space or any of the following characters.\n!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n")
    while special not in string.punctuation or special == "":
        special = input("That was not a special character. Please enter either a space or any of the following "
                        "characters.\n!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n")
    return special


def generate_secure_passphrase(c, d):
    passphrase = []
    for i in range(c):
        randomword = random.choice(lists.Words)
        passphrase.append(randomword + d)
    print("Your secure passphrase is:\n" + lists.colour.RED + "".join(passphrase) + "\n")
    time.sleep(pause)
    print(lists.colour.END + lists.Strength[c - 2])


generate_secure_passphrase(get_length(minimum, maximum), get_special())
