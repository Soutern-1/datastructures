def calculate(index):

    if index < 0 or index == 0:
        print("Enter a number that is greater than zero ad not equal to zero")
    elif index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return calculate(index - 1) + calculate(index - 2)

index = int(input("Enter Index: "))
result = calculate(index)
print(result)

# 1-0, 2-1, 3-1, 4-2, 5-3, 6-5, 7-8, 8-13, 9-21, 10-34, 11-55, 12-89, 13-144 
