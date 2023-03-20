import random

Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = Uppercase.lower()
Number = "1234567890"
Symbols = "!@#$%^&*()_-+-/\\"

all = ""
upper , lower , numer , symbol = True, True, False, True

if upper:
    all += Uppercase
if lower:
    all += Lowercase
if numer:
    all += Number
if symbol:
    all += Symbols

pswrd_lenth = 40
numberofpswrds = 10

for i in range(numberofpswrds):
    pswrd = ''.join(random.sample(all,pswrd_lenth))
    print(pswrd)

