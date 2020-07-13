import string
import random

def generate():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    try:
        passlen = int(input('Enter length for the password: '))
        s = list()
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        
        random.shuffle(s)    

        password = ("".join(s[0:passlen]))
        print(password)
        
    except:
        print('Enter an integer')

generate()
