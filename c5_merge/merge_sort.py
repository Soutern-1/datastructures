list = [32,56,12,13,95,51,86,5,41,88,10,40,54,100]

def merge(left_list,right_list):
    sorted_list = []
    i=0
    j=0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    if i < len(left_list):
        sorted_list.append(left_list[i:])
    if j < len(right_list):
        sorted_list.append(right_list[j:])

    return sorted_list



def seperate_list(list):
    # this will divide the list into sublists
    # it will be recursive
    if len(list) <= 1:
        return list
    midpoint = int(len(list) // 2)
    left_list = list[:midpoint]
    right_list = list[midpoint:]
    
    sub_left_list = seperate_list(left_list)
    sub_right_list = seperate_list(right_list)

    return merge(sub_left_list,sub_right_list)

new_list = seperate_list(list)

print(new_list)