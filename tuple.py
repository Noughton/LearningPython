#元组

classmate = ('stone','hero','mid') #元组的用法和列表相似
print(classmate)

print(len(classmate)) #列表同理，获得元组的长度
print(classmate[-1])  #列表同理，负数角标取值

#classmate[1] = 'transfrom' #元组类似静态常量，赋值之后不可修改
#classmate.append('hello') #元组不支持追加元素
#classmate.insert('world') #元组不支持插入元素
#classmate.pop() #元组不支持删除元素

newTuple = ('new') #元组只定义一个元素时()被定义为数学符号，所以此处为常量
print(newTuple)
newTuple_double = ('tuple',) #元组需要定义单一元素时需在元素后添加','，输出时也会显示','
print(newTuple_double)
newTuple_thired = () #元组可以定义为空
print(newTuple_thired)

#可变元组

changeTuple = ('锤子',['宝子',23]) #元组中可添加列表元素
print(changeTuple)
changeTuple[1][0] = '犊子' #此处赋值的为元组内部的列表，元组为可赋值容器，此处changeTuple[1]指向的为地址，不会限制容器特性
print(changeTuple)