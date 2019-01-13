#'silce' 切片
silce_list = ['锤子','犊子','宝子']
print(silce_list[0:2]) #角标使用':'分割，实现切片功能[切片起点:切片结尾+1]
print(silce_list[:2])  #切片起点为0时可以省略

print(silce_list[-1:]) #切片支持角标倒叙

print(silce_list[0:3:2]) #间隔取值[切片起点:切片结尾+1:取值间隔]

silce_tuple = ('233','333','433')
print(silce_tuple[:2]) #'tuple'也可以使用切片

silce_str = 'Beijing'
print(silce_str[:3]) #'string'也可以使用切片功能