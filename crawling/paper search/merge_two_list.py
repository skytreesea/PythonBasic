

list1 = ['w','j']
list2 = [1,2]
     
def make_list_to_dict(list1, list2):
    result = {}
    if len(list1) == len(list2):
        for i in range(len(list1)):
            result[list1[i]]=list2[i]
    return result
    
print(make_list_to_dict(list1,list2))