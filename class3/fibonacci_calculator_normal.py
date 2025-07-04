index = int(input("Enter index: "))
# n1 and n2 are always 0 1 
if index > 0 or index == 0:
    print("Enter a number that is greater than zero ad not equal to zero")
elif index == 1:
    print(0)
elif index == 2:
    print(1)
else:
    sequence = [0, 1]
    for i in range(2, index):
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence[-1])
    print(sequence)


# 1-0, 2-1, 3-1, 4-2, 5-3, 6-5, 7-8, 8-13, 9-21, 10-34, 11-55, 12-89, 13-144
