import sys
import string
import random


def strength_check(passwd):
    has_ascii = any(char in passwd for char in string.ascii_letters)
    has_digits = any(char in passwd for char in string.ascii_letters)
    has_punctuation = any(char in passwd for char in string.punctuation)
    return (has_ascii + has_digits + has_punctuation)

def generate():
    if len(sys.argv) > 2:
        print("[usage] python spg.py <length (optional)>")
        sys.exit()
    try:
        length = sys.argv[1]
    except IndexError:
        length = 12

    try:
        length = int(length)
        if length < 1:
            print("length must be bigger than 0")
            sys.exit()

        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = "" 
        

        while not strength_check(password): 
            for i in range (length):
                password += random.choice(alphabet)

        print (password)
    except ValueError:
        print ("length must be a number")


if __name__ == "__main__":
    generate()
