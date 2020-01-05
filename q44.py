uc,lc,a,d = 0,0,0,0
s = input("Enter a string \n")
for i in range(len(s)):
    if s[i].isupper():
        uc+=1
    if s[i].islower():
        lc+=1
    if s[i].isalpha():
        a+=1
    if s[i].isdigit():
        d+=1
print("Uppercase letters = {0} \nLowercase letters = {1} \nAlphabetic characters = {2} \nDigits = {3}".format(uc,lc,a,d))