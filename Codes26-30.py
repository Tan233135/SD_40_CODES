#26. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))
lst=list(map(int, input("Enter the list:  ").split()))
print(f"The list after removing duplicates {remove_duplicates(lst)}")
#27. Flatten a nested list
def flatten(nested_lst):
    return [item for sublist in nested_lst for item in sublist]
nested_lst=[]
n=int(input("Enter the number of sublists:  "))
for i in range(n):
    sublist = list(map(int , input(f"Enter the elements of sublist {i+1}:  ").split()))
    nested_lst.append(sublist)
flattened_list=flatten(nested_lst)
print(f"The flattened list is: {flattened_list}")
#28. check if a list is empty
def is_empty(lst):
    return len(lst)==0
lst=list(map(int, input("Enter a list:  ").split()))
if is_empty(lst):
    print("The list is empty")
else:
    print("The list is not empty")
#29.Intesections of two sets
def intersection(set1,set2):
    return set1 & set2
set1=set(map(int,input("Enter the elements of the first set: ").split()))
set2=set(map(int, input("Enter the elements of 2nd set: ").split()))
print(f"The intersection of two sets is : {intersection(set1, set2)}")
#30. print dictionary
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")
n=int(input("Enter the number of key value pairs: "))
d={}
for _ in range(n):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=value 
print("The dictionary contains: ")
print_dict(d)