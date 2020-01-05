#MoThErFuCkIn cAmEl cApS

s=input("Enter a string\n")
x=''
for i in range(len(s)):
    if i%2==0:
        x+=s[i].upper()
    else:
        x+=s[i]
print(x)