#31.Merge two dictionaries 
def merge_dicts(dict1,dict2):
    return {**dict1,**dict2}
n1=int(input("Enter the number of key value pairs for the first:  "))
dict1={}
for _ in range(n1):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    dict1[key]=value
n2=int(input("Enter the number of key_value pairs for the 2nd: "))
dict2={}
for _ in range(n2):
    key=input("Enter the key: ")
    value =input("Enter the value: ")
    dict2[key]=value 
merged_dict=merge_dicts(dict1,dict2)
print("The merged dictionary is: ")
for key, value in merged_dict.items():
    print(f"{key}: {value}")
#32. Remove item from dictionary
def remove_item(d,key):
    d.pop(key,None)
    return d 
n=int(input("Enter the number of key_value pair: "))
d={}
for _ in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key]=value
print("Original dictionary: ",d)
key_to_remove=input("Enter the key to remove: ")
updated_dict=remove_item(d,key_to_remove)
print("Updated dictionary: ", updated_dict)
#33.lamda function example 
square = lambda x: x**2
n=int(input())
print(f"The square of {n} is {square(n)}")
#34.sort dictionary by value
def sort_dict(d):
    return dict(sorted(d.items(),key=lambda item: item[1]))
n=int(input("Enter the key-value pair: "))
d={}
for _ in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=int(value)
sorted_dict=sort_dict(d)
print("sorted dict: \n",sorted_dict)
#35. char frequency counter
from collections import Counter
def char_frequency(s):
    return dict(Counter(s))
s=input()
frequency=char_frequency(s)
print("Character frequency: ")
for char, freq in frequency.items():
    print(f"{char}: {freq}")