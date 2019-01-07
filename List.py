#列表

university = ["数字艺术系","计算机科学与技术系","软件工程系"]
print(university)
print(len(university)) #列表长度

print(university[0]) #列表可以使用角标读取
print(university[1]) #角标的始位为0
print(university[2]) #列表的末位为len('List') - 1

print(university[-1]) #角标"-1"也代表列表末位
print(university[-2]) #倒数第二
print(university[-3]) #倒数第三
#print(university[-4]) #此处越界

university.append("英语系") #列表末尾追加元素
print(university)

university.insert(1,"继续教育学院") #列表插入元素(位置，元素)
print(university)

university.pop() #删除列表末尾元素
print(university)

university.pop(2) #删除列表制定位置元素(位置)
print(university)

university[1] = "国际教育学院" #指定列表位置赋值
print(university)

student = ['锤子',23,120.3,False] #列表中的元素类型可不相同
print(student)

classRoom = ['犊子',student,'宝子'] #列表中可以看包含另外一个列表
print(classRoom)
print(classRoom[1][0]) #类似二维数组

bashRoom = [] #此处为一个空列表，长度为0
print(bashRoom)
print(len(bashRoom))