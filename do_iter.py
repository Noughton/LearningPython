#'iter' 迭代

iter_list = ['锤子','剪子','宝子','犊子','斧子']

for v in iter_list:
    print(v)

iter_dist = {'name' : '锤子','age' : 23,'address' : 'Beijing'}

for k in iter_dist: #默认迭代'dist'的'key'
    print(k)

for v in iter_dist.values(): #迭代'dist'的值
    print(v)

for k,v in iter_dist.items(): #迭代'dist'的整体
    print(k,':',v)

for v in 'Beijing':
    print(v)

from collections import Iterable #判断容器能否被迭代
print(isinstance('Beijing',Iterable))
print(isinstance(iter_list,Iterable))
print(isinstance(iter_dist,Iterable))
print(isinstance((1,2,3),Iterable))

iter_duo_list = [(1,0),(2,1)]

for v1,v2 in iter_duo_list:
    print(v1,v2)