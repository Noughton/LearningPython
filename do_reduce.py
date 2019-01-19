#'reduce'序列执行
from functools import reduce

def f(x,y):
    return x + y

reduce_num = reduce(f,[1,2,3,4]) #'reduce'的执行方式为f(f(f(1,2),3),4)
print(reduce_num)

