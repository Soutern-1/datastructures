list = [12,23,25,36,39,40,44,45,50,59,61,62,67,70,89,91,93,100]

input = int(input("What is the input number: "))

start = 0
end = len(list) -1
mid = (start + end) // 2

while input != int(list[mid]) and start < end:
    if input > int(list[mid]):
        # change the start
        start = mid + 1
        mid = (start + end)//2
        print(f"Input > Mid{start, mid ,end}")

    elif input < int(list[mid]):
        # change the end
        end = mid - 1
        mid = (start + end) // 2
        print(f"Input < Mid{start, mid ,end}")

    
 
if input == int(list[mid]):
    print(f"Found at index: {mid+1}")
else:
    print("Eleemnt not in list")


