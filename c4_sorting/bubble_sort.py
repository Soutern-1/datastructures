list = [32,56,12,13,95,51,86,35,41,88,10,40,54]

list_length = len(list)
in_order = False


while not in_order:
    count = 0
    for index in range (len(list)-1):
        if list[index] > list[index+1]:
            num = list[index]
            list[index] = list[index+1]
            list[index+1] = num
            count +=1
            in_order = False

    if count == 0:
        in_order = True
            


print(list)