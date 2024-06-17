#
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3 #
reuslt = []

#
sub_list = []

for element in num_list: #duyệt theo giá trị
    sub_list.append(element)
    
    if len(sub_list) == k:
        print(sub_list)
        del sub_list[0]
        maxNumber = max(sub_list)
        print(f"{sub_list} have max is {maxNumber}")
        
