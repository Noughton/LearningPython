#定制类

class Student(object):
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return 'Student object(name: %s)' %self.name

    __repr__ = __str__

stone = Student('锤子')
print(stone)

#迭代

class Student_1():
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

def fib():
    for n in Student_1():
        print(n)

fib()

#调用实例

class Student_2():
    def __call__(self):
        print('This is call!')

s = Student_2()
s()

#自定义角标访问方法
class Student_3():
    def __getitem__(self,n):
        a, b = 1, 1
        for x in range(n):
             a, b = b, a + b
        return a

f = Student_3()
print(f[0])

#返回未定义属性
class Student_4():
    def __init__(self):
        self.name = '锤子'

    def __getattr__(self,attr):
        if attr == 'age':
            return 25
        raise AttributeError('don\'t have %s' % attr)

st = Student_4()
print(st.name)
print(st.age)
print(st.address)