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
#8. Factorial
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
x=int(input())
print(f"The factorial is {factorial(x)}")
#9. swap two variable
def swap(a,b):
    return b,a 
a=int(input())
b=int(input())
print(f"The swapped values are {swap(a,b)}")
#10. palindrome check
def is_palindrome(s):
    return s==s[::-1]
s=input()
if is_palindrome(s):
    print(f"{s} is palindrome")
else:
    pritn(f"{s} is not palindrome")

