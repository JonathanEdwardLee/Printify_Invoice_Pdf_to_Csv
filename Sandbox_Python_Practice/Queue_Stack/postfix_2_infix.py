# Jonathan Lee


from Queue import Queue
from Stack import Stack

def p2i(q):
    temp_s = Stack([]) 

    while not q.is_empty():
        char = q.deq()
        if char in ("+", "-", "*", "/"):
            op2 = temp_s.pop()
            op1 = temp_s.pop()
            temp_s.push("(" + op1 + " " + char + " " + op2 + ")")
        else:
            temp_s.push(char)

    return temp_s.pop()

print(p2i(Queue(["1", "2", "+"])))  # Expected output: (1 + 2)
print(p2i(Queue(["5", "4", "*", "7", "+"])))  # Expected output: ((5 * 4) + 7)
print(p2i(Queue(["2", "3", "*", "8", "5", "*", "+"])))  # Expected output: ((2 * 3) + (8 * 5))
#p2i(Stack([1, 2, +])).print() #Q[1 + 2]
#p2i(Queue( [5 4 * 7 +] )).print() #Q[5 * 4 + 7]
#p2i(Queue( [2 3 * 8 5 * +] )).print() #Q[2 * 3 + 8 * 5]