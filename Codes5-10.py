import math
#6.Prime check
def is_prime(num):
    if num<2:
        return "not prime"
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return "not prime"
    return "prime"
n=int(input())
print(f"The number is {is_prime(n)}")
#7. Fibonacci sequence
def fibonachhi(n):
    fib_seq=[0,1]
    for i in range(2,n):
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq[:n]
x=int(input())
print(f"The sequence is {fibonachhi(x)}")