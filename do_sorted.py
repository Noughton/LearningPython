#'sorted'排序序列

sorted_list = [2,6,3,-1,-26]
sorted_list_01 = sorted(sorted_list)
print(sorted_list_01)

sorted_list_02 = sorted(sorted_list,key = abs) #排序函数会根据'key'的函数规则进行排序
print(sorted_list_02)

sorted_list_str = ['dfa','efd','afg']
sorted_list_03 = sorted(sorted_list_str) #排序规则时根据'ascii'编码表进行排序
print(sorted_list_03)

sorted_list_04 = sorted(sorted_list_str,reverse = True) #排序中添加参数'reverse'为'True'时为倒叙
print(sorted_list_04)