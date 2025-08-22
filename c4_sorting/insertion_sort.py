list = [32,56,12,13,95,51,86,5,41,88,10,40,54]


# if list(starting_index) < list(starting_index-1):

#     while list(starting_index) < list(checking_index):
#         checking_index-=1
#         if checking_index > 0:
#             break


for index in range(1,len(list)):
    check_index = index-1
    temp = list[index]
    while temp < list[check_index] and  check_index >= 0:
        list[check_index+1] = list[check_index]
        check_index-=1
    list[check_index+1] = temp

print(list)        
        


