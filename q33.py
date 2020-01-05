i = input("Enter integer more than 1000 ")
x = ''
for j in range(1,len(i)+1):
    x += i[-j]
print(x)