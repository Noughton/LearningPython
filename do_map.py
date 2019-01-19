#'map' 图

def map_fun(x,y,f): #高级函数特性，函数可作为参数调用
    return f(x) + f(y)

abs_map = map_fun(-5,6,abs)
print(abs_map)

def f(x):
    return x*x

abs_map_01 = map(f,[1,2,3]) #'map'中的第一个参数为函数对象本身
abs_list = list(abs_map_01) #'abs_map_01'为一个惰性序列'Iterable'，需要使用'List'函数转换为'list'
print(abs_list)

