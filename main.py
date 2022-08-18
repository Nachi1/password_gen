# This is a simple Python script to generate a password
import random
import string

password_dict = {}


class PasswordGenerator:
    @staticmethod
    def password_gen():
        # Main program starts here
        # 3 uppercase, 4 lowercase, 2 numbers
        uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
        uppercaseLetter2 = chr(random.randint(65, 90))  # Generate a random Uppercase letter (based on ASCII code)
        lowercaseLetter1 = chr(random.randint(97, 122))
        lowercaseLetter2 = chr(random.randint(97, 122))
        uppercaseLetter3 = random.choice(string.ascii_uppercase)
        lowercaseLetter4 = random.choice(string.ascii_lowercase)
        lowercaseLetter5 = random.choice(string.ascii_lowercase)
        # digit1 = random.randint(0, 9 + 1)
        d2 = string.digits
        special_chr = chr(random.randint(32, 47))
        special_chr2 = chr(random.randint(32, 47))

        # Generate password using all the characters, in random order
        passWord = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter5 + \
                   lowercaseLetter4 + lowercaseLetter2 + lowercaseLetter1 + uppercaseLetter3 + \
                   special_chr + d2 + special_chr2

        password_list = list(passWord)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password


def password_logic():
    pw = r.password_gen()
    while True:
        print('type "yes" to generate a password')
        ans1 = input('>> ')
        if ans1 == 'yes':
            break
        elif ans1 == '':
            return
        else:
            print('invalid input')
            print('yes to continue or " " to quit')
            return password_logic()
    platform = input('enter the app or account name you wish to save the password for\n'
                     '>> ').lower()
    password_dict[platform] = pw
    print(password_dict)


r = PasswordGenerator()
password_logic()

# next project is to create a memory dictionary
