#36.Map two lists to a dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
keys=input("Enter the keys: ").split()
values=input("Enter the values: ").split()
if len(keys) != len (values):
    print("Error ")
else: 
    values=[int(v) for v in values]
    result_dict=lists_to_dict(keys,values)
print("Mapped dictionary: ", result_dict)
#37. Implementing a stack using list
class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
my_stack=stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Pooped item: ", my_stack.pop())
print("Pooped item: ", my_stack.pop())
#38. Implementing a queue using list
class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
my_queue=queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print("Dequeue item: ", my_queue.dequeue())
print("Dequeue item: ", my_queue.dequeue())
print("Dequeue item: ", my_queue.dequeue())
print("Dequeue item: ", my_queue.dequeue())