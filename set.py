#'set'集合
#'set'是一个只有'key'的集合容器

set_list = set([1,2,3]) #'set'赋值时需要使用'list'表示
print(set_list)

set_list.add(4) #'set'可使用'add'的方法为集合添加元素,'add'不可添加'list'
print(set_list)

set_list.add(3) #'set'中不可以出现重复元素
print(set_list)

set_list.remove(3) #使用'remove'删除集合中的元素
print(set_list)