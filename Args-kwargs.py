# args-kwargs
'''
def sum_list(my_list):
    s = 0
    for i in my_list:
        s +=i
    return  s

li = [1,2,3,4,9]
print (sum_list(li))
'''
def sum_args(*args):
    ss = 0
    for i in args:
        ss += i
    return ss

print (sum_args(1,2,3,4))
