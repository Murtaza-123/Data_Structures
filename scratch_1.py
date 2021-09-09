class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # EnQueue item to the queue
    def enQueue(self, x):
        self.stack1.append(x)

    # DeQueue item from the queue
    def deQueue(self):
        # if both the stacks are empty
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Q is Empty")
            return



        # if stack2 is empty and stack1 has elements
        elif len(self.stack2) == 0 and len(self.stack1) > 0:
            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()

        else:
            return self.stack2.pop()

    # Driver code

if __name__ == '__main__':
    # q.stack1.append(1)
    # q.stack1.append(2)
    # q.stack1.append(3)

    # print(q.stack.pop()) # prints 3
    # print(q.stack.pop()) # prints 2
    # print(q.stack.pop()) # prints 1
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
