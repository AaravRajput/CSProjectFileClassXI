s=input("Enter a string\n")
v=['a','e','i','o','u']
c=''
for i in range(len(s)):
    if not s[i] in v:
        c+=s[i]
print(c)