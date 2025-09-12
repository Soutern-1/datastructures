class Queue():
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.max = 10
    def enqueue(self,input):
        if len(self.queue)  >= 10:
            print("Queue is full, item not added.")
            print(self.queue)        
        else:
            self.queue.append(input)
            self.tail = len(self.queue)
            print(f"Current queue is {self.queue}, and current tail is {self.tail}")
        
    def dequeue(self):
        
        if len(self.queue) == 0:
            print("No items in queue to remove. ")
        else:
            for i in range(len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            print(f"Current queue is {self.queue}")

que = Queue()

def main():
    print("----------------=-------------")
    inp = str(input("Options - Eq, Dq, Stop: "))
    if inp == "Eq":
        inpu = input("Enter item to append: ")
        que.enqueue(inpu)
        main()
    elif inp == "Dq":
        que.dequeue()
        main()
    elif inp == "Stop":
        print("Program Stopped.")
        print(f"Final queue:{que.queue}")
    else:
        print("Incorrect operation, try again")
        main()
main()