#1.Hello world
print("Hello world")
#2.Sum of two numbers
def sum_two_num(a,b):
    return a+b

a=int(input())
b=int(input())
print(f"Sum of {a} and {b} is {sum_two_num(a,b)}")
#3. Sqare root of a number
import math
def sqrt_num(n):
    return math.sqrt(num)
x=int(input())
print(f"The sqare root of {x} is {sqrt_num(x)}")
#4.Triangle area
def tri_area(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
a=int(input())
b=int(input())
c=int(input())
print(f"The area of the triangle is {tri_area(a,b,c)}")
#5.Even or odd
def even_odd(x):
    if x%2==0:
        return "Even"
    else:
        return "ODD"
x=int(input())
print(f"The number is {even_odd(x)}")

