'''
1 + x + x^2 + x^3 + x^4 + ... + x^n
GP with common ratio x
sum of GP = a(r^n-1)/(r-1)
'''
x = int(input("Enter common ratio "))
n = int(input("Enter no. of terms "))
sum = 1*((x**n)-1)/(x-1)
print("Sum of GP is ", sum)