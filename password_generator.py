import string
import random
from ntpath import join
import numbers

numbers = "0123456789"
chars_low = "abcdefghijklmnopqrstuvwxyz"
chars_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$.,_-/\|"

password = []
for i in range( int (input("Enter the length of the password: ") ) ):
    password.append(random.choice(chars_low + chars_up + symbols))
random.shuffle(password)
print("".join(password))
    

    
    