#偏函数

import functools

int2 = functools.partial(int,base = 2)
H2D = int2('A',base = 16)
print(H2D)

def person(name,age,sex):
    print('这是我的%s,他叫%s,他今年%d' %(sex,name,age))

myPerson = functools.partial(person, age = 30, sex = '爸爸')
#myPerson = functools.partial(person,sex = '爸爸') #偏函数定义额默认参数为倒数n个参数
#myPerson = functools.partial(person)

myPerson('留名')
#myPerson('留名',30)
#myPerson('留名',30,'爸爸')