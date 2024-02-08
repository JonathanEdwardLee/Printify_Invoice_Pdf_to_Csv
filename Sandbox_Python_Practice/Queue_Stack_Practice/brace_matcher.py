#Jonathan Lee

from Stack import Stack
from Queue import Queue

def matcher(s):
    stack = Stack([])
    open = ("([{")
    close = (")]}")
    for char in s:
        
        if char in open:
            stack.push(char)
        elif char in close:
            if stack.is_empty():
                return False
            top_item = stack.pop()
            if open.index(top_item) != close.index(char):
                return False
    return stack.is_empty()


print(matcher("[()]")) #True
print(matcher("[(")) #False
print(matcher("hello")) #True

# without using index method
# def matcher(s):
#     stack = Stack([])
#     for char in s:
#         if char in "([{":
#             stack.push(char)
#         elif char in ")]}":
#             if stack.is_empty():
#                 return False
#             top_item = stack.pop()
#             if (top_item == '(' and char != ')') or \
#                (top_item == '[' and char != ']') or \
#                (top_item == '{' and char != '}'):
#                 return False
#     return stack.is_empty()