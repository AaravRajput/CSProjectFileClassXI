x = input("Enter a character ")
if x.isupper():
    print("Uppercase")
elif x.islower():
    print("Lowercase")
elif x.isdigit():
    print("Digit")
else:
    print("Special character")