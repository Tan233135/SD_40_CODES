#11. Find the maximum and minimum in a list
def max_min(numbers):
    return max(numbers),min(numbers)
numbers=list(map(int,input("Enter a list").split()))
maximum, minimum = max_min(numbers)
print(f"The maximum value is {maximum}")
print(f"The minimum value is {minimum}")
#12. GCD and LCM
import math 
def gcd_lcm(a,b):
    gcd=math.gcd(a,b)
    lcm=abs(a*b)//gcd 
    return gcd,lcm
a=int(input())
b=int(input())
print(f"The gcd and lcm are {gcd_lcm(a,b)}")
#13. Temperature conversion 
def c_to_f(c):
    return (c*9/5)+32
def f_to_c(f):
    return (f-32)*5/9
c=float(input("Temperature in celcius:"))
f=float(input("Temperature in ferenheit:"))
print(f"{c} in ferenheit is {c_to_f(c)}")
print(f"{f} in celcius is {f_to_c(f)}")
#14. Generate a random number:
import random
def random_number(start,end):
    return random.randint(start,end)
start=int(input("Enter the lowest number"))
end=int(input("Enter the highest number"))
print(f"The random number between {start} and {end} is {random_number(start,end)}")
#15. sum of a list
def sum_list(lst):
    return sum(lst)
lst=list(map(int, input("Enter a list").split()))
print(f"The sum of {lst} is {sum_list(lst)}")