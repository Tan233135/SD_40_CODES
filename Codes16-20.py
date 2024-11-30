import math
import random
#16. Count vowels in a string
def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")
s=input("Enter a string")
print(f"The string {s} have {count_vowels(s)} vowels")
#17. Remove punctutations from a string
import string
def remove_punc(s):
    return s.translate(str.maketrans('','',string.punctuation))
x=input("Enter a string:  ")
print(f"The string {x} without punctuation is {remove_punc(x)}")
#18. ASCII value of a character
def ascii_value(char):
    return ord(char)
c=input()
print(f"The ASCII value of {c} is {ascii_value(c)}")
#19. Reverse a number
def reverse_number(num):
    return int(str(num)[::-1])
num=input()
print(f"The reverse of {num} is {reverse_number(num)}")
#20. Find the second largest number in a list
def second_largest(lst):
    unique_lst=list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >=2 else None
lst=list(map(int, input("Enter a list:  ").split()))
print(f"The second largest in {lst} is {second_largest(lst)}")