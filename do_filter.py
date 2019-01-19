#'filter'过滤序列

def is_odd(x):
    return x % 2 == 1

filter_odd = list(filter(is_odd,[x for x in range(10)])) #'filter'会过滤第一个参数中函数返回为'false'的值
print(filter_odd)
