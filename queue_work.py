# create a class called Queue. The class should have the following methods: enqueue, 
# dequeue, and size. The enqueue method should add an item to the queue. The dequeue 
# method should remove an item from the queue. The size method should return the size 
# of the queue.




class Queue:
    queue_1 = list()
    max_length = 10

    def enqueue(self,item):
        self.item = item
        # only add a item if the list is less than max length
        if len(self.queue_1) < self.max_length:
            self.queue_1.insert(0,item)
            return self.queue_1
        else:
            return 'queue is full. cant add item'


    def dequeue(self):

        if len(self.queue_1) != 0:
            return self.queue_1.pop()
            
        else:
            return 'queue is empty. cant remove from nothing'

    def size(self):
        return f'queue size : {len(self.queue_1)}'



qu = Queue()

print(qu.enqueue(6))
qu.enqueue(6)
print(qu.size())