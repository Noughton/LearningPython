#函数

#'def'为定义函数的关键字
def add(x,y):
	return x + y

print(add(1,2))

#多返回函数
def division(x,y):
	return x/y ,x%y

w,v = division(5,2) #函数的返回值是以'tuple'的形式返回的，在赋值时会分别将值赋值给变量
print(w,v)

u = division(7,2) #当把多返回函数的返回值赋值给一个容器时，该容器为'tuple'
print(u)

#可变参数函数
def adds(*nNum): #可变参数只需要填写一个参数，但需要在参数前添加'*'以表示可变参数
	print(nNum) #可变参数以'tuple'的格式传递，为不可变参数
	nSum = 0
	for x in nNum:
		nSum = nSum + x
	return nSum

print(adds(1,2,3))
print(adds(*(1,3))) #当直接传递'list','tuple'为多参数时，需要在容器前添加'*'以表示可变参数

#关键字参数
def info(**role): #关键字参数需要添加'**'以表示当前参数为关键字参数
	print(role)

info(**{'name':'锤子','age':23,'isLive':True}) #关键字参数在以'dist'作为参数直接传递的时候需要添加'**'以表示关键字参数

#命名关键字参数
def all_info(name,age,*,islive,address):
	print(name,age,islive,address)

all_info('锤子',23,islive=True,address='Beijing')

def all_info_dou(name,age,*birthday,islive,address):
	print(name,age,birthday,islive,address)

all_info_dou('锤子',23,1994,8,25,islive = True,address = 'Beijing')