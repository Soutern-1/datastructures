class Queue():
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.max = 10

    def enqueue(self):
        # remove a car into the car park, add one slot
        if len(self.queue) >= self.max:
            print("No cars in parking lot")
        else:
            flag = False
            # PROBLEM
            for i in range(11):
                if str(i) not in self.queue and flag == False:
                    self.queue.append(i+1)
                    flag = True

            # PROBLEM

            self.tail = len(self.queue)

    def dequeue(self):
        # add a car from the car park, remove one slot
        if len(self.queue) == 0:
            print("Parking is at full curently,")
        else:

        
            for i in range(len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()
            print(f"Current parking available is {len(self.queue)},{self.queue}")
        



# fill queue with all slots (to show all spaces are empty, then start removing slots)
parking_slots = Queue()
for i in range(1, 11):
    parking_slots.queue.append(i)



def main():
    while True:
        print("----------------")
        print("1: Park a car, 2: Remove a car, 3: show available slots")

        choice = input("Enter your choice: ")

        if choice == "1":
            parking_slots.dequeue()
            print("Car added")
            # print(f"Available parking spaces: {parking_slots.queue}")
            main()
        elif choice == "2":
            parking_slots.enqueue()
            print("car Removed")
            print(f"Available parking spaces: {len(parking_slots.queue)},{parking_slots.queue}")
            main()
        elif choice == "3":
            print(f"Available parking spaces: {len(parking_slots.queue)},{parking_slots.queue}")
            main()
        else:
            print("Invalid choice.")
            main()

main()