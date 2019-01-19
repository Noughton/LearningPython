#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5)
sum_list_num = f()
print(sum_list_num)

#闭包
def count(): #注意闭包中最好不要出现循环
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count() #闭包中出现循环，由于程序是后置执行的，此时循环已经结束了，所以以变量的最终结果执行
fi_list = f1()
print(fi_list)
f2_list = f2()
print(f2_list)
f3_list = f3()
print(f3_list)

def count_01():
    fs = []
    def g(j):
        def f():
            return j * j
        return f
    for n in range(1,4):
        fs.append(g(n))
    return fs

f4,f5,f6 = count_01() #如果闭包中一定要存在循序，需要在闭包执行函数外面加套一层函数，并将此时的变量存入函数，此时的函数就会遍历执行
f4_list = f4()
print(f4_list)
f5_list = f5()
print(f5_list)
f6_list = f6()
print(f6_list)