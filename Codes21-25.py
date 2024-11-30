#21. sort a list in ascending/ descending order
def sort_list(lst,ascending=True):
    return sorted(lst,reverse=not ascending)
lst=list(map(int, input("Enter a list:   ").split()))
print(f"ascending order {sort_list(lst)}")
#22.Merge two lists
def merge_lists(lst1,lst2):
    return lst1+lst2
lst1=list(map(int,input("Enter the 1st list:   ").split()))
lst2=list(map(int, input("Enter the 2nd list: ").split()))
print(f"The merged list is {merge_lists(lst1,lst2)}")
#23. Common elements of two lists
def common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))
lst1=list(map(int,input("Enter the 1st list: ").split()))
lst2=list(map(int,input("Enter 2nd list: ").split()))
#24. sum of all elements of a list 
def sum_elements(lst):
    return sum(lst)
lst=list(map(int, input("Enter the elements: ").split()))
print(f"The sum is {sum_elements(lst)}")
#25. count ocurrences of each element in a list
from collections import Counter
def count_occurences(lst):
    return dict(Counter(lst))
lst=list(map(int,input('Enter the list: ').split()))
print(f"The occurences are {count_occurences(lst)}")