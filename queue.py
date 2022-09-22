list_1 = list()
maximum = 5

def isEmpty():
    return len(list_1) == 0    



def isFull():
    return len(list_1) == maximum

def enqueue(element):
    if not isFull():
        list_1.insert(0,element)
        return list_1
    else:
        return 'list is already full'


def dequeue():
    if not isEmpty():
        list_1.pop()
        return list_1

    else:
        return 'yo the list is already empty'

def display(f):
    print(f)

display(enqueue(6))
display(enqueue(7))
display(enqueue(8))
display(enqueue(9))
display(enqueue(10))
display(isFull())
display(enqueue(1))