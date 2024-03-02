# Jonathan Lee
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node("First node")
node2 = Node("Second node", node1)
node3 = Node("Third node", node2)
node4 = Node("Fourth node", node3)

n = node4
while n is not None:
    print(n.data,"->", end=" ")
    n = n.next

print(" ")

def print_list(head):
    n = head
    while n is not None:
        print(n.data,"->", end=" ")
        n = n.next
    print("None")

node3.next = node1 #removes node2
print_list(node4)
node5 = Node("New node", node4)
print_list(node5)
print_list(node3)
