# Jonathan Lee

from Queue import Queue
from Stack import Stack

def flip(s):
    temp_s = Stack([])

    while not s.is_empty():
        temp_s.push(s.pop())
    

          

    
    return temp_s

flip(Stack([1,2,3,4])).print()
