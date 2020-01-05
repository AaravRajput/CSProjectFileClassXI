j = 0
a = 1
while j<=10:
    b = (2**a)-1
    isPrime = True
    for i in range(2,b):
        if b%i==0:
            isPrime=False
            break
    if isPrime == True:
        print(b)
    
    a+=1
# After 8th Mersenne no. the digits are too high for python to calculate and thus results in hanged process
# Also I guess there is something wrong with Q. No.35 & 36 as in Q.36 We are told to write prime in front of Mersenne numbers that are prime
# However Mersenne no.s ARE prime
#Basically Mersenne no.s are those prime numbers that are 1 less than a power of 2
#For example 3 (a prime no.) is 1 less than 4 which is a power of 2
