# create a class called Stack. The class should have the following methods: push, pop,
#  and size. The push method should add an item to the stack. The pop method should remove
#  an item from the stack. The size method should return the size of the stack.

class Stack:
    stack_1 = list()
    max_length = 10


    def push(self,item):
        self.item = item

        if len(self.stack_1) < self.max_length:
            self.stack_1.append(self.item)
            return self.stack_1

        else:
            return 'stack is full,cant add new item'


    def pop(self):
        if len(self.stack_1) != 0:
            return self.stack_1.pop()

        else:
            return "cant pop an empty stack"

    def size(self):
        return f'stack size : {len(self.stack_1)}'

stk = Stack()
stk.push(6)
stk.pop()
print(stk.size())
