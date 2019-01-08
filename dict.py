#'dist' 字典

myDist = {'name':'锤子','age':23,'sex':'man'} #'dist'采用键值对的表现形式'key - value'
print(myDist['name'])
print(myDist['age'])
print(myDist['sex'])
#'dist'相比'list'会占用较多内存，但速度会很快
#'dist'的查询方式类似字典，会先通过'key'计算出'value'的内存地址
#'dist'中的'key'为不可变值，所以不能使用'list'这种可变列表作为'key'

myDist['age'] = 25 #'dist'的值可以通过'key'赋值改变
print(myDist['age'])

#myDist['class'] #'list'中不能使用不存在的'key'
if 'class' in myDist: #使用'in'可以检测出'dist'中是否存在此'key'
	print('存在')
else:
	print('不存在')

print(myDist.get('class',-1)) #'get'检测'dist'中是否存在此元素，('key',err),'err'可忽略

myDist.pop('age') #删除指定'key'的元素
print(myDist)

#'dist'为非顺序容器