# Jonathan Lee

from Queue import Queue

def count_uniq(q):
    if q.is_empty():
        return 0
    
    count = 0
    last = None

    while not q.is_empty():
        current = q.deq()
        if current != last:
            count += 1
            last = current
    return count

print(count_uniq(Queue( [1,1,1,2,2,4,4,4,6] ))) #4
print(count_uniq(Queue( [3,0,4,4,4,7,7,5,5,5,5] ))) #5
print(count_uniq(Queue( [ ] ))) #0
