#Check if first and last number of list is same
def is_first_and_last_same(list):
    return list[0] == list[-1]
my_list  = [10,20,30,40,10]
result = (is_first_and_last_same(my_list))
print (result)