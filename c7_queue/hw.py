class Queue():
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.max = 10
    def enqueue(self,input):
        if len(self.queue)  >= 10:
            print("Queue is full, item cannot be not added.")
            print(self.queue)        
        else:
            self.queue.append(input)
            self.tail = len(self.queue)
            print(f"Current queue is {self.queue}")
        
    def dequeue(self):
        
        if len(self.queue) == 0:
            print("No items in printing queue to print. Add items and then try again. ")
        else:
            for i in range(len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            if self.queue == []:
                print("Printer Queue is currently empty!")
            
            else: 
                print("Item successfully printed!")
                print(f"Current queue is {self.queue}")


que = Queue()

def main():
    print("----------------=-------------")
    inp = str(input("Options - Add, Print, Stop: "))
    if inp == "Add":
        inpu = input("Enter item to print: ")
        que.enqueue(inpu)
        main()
    elif inp == "Print":
        que.dequeue()
        main()
    elif inp == "Stop":
        print("Program Stopped.")
        print(f"Final queue:{que.queue}")
    else:
        print("Incorrect operation, try again")
        main()
main()
