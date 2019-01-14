#列表生成式

listcompr_01 = list(range(1,11))
print(listcompr_01)

listcompr_02 = [x for x in range(1,10)]
print(listcompr_02)

listcompr_03 = [x * x for x in range(1,10)]
print(listcompr_03)

listcompr_04 = [x for x in range(1,10) if(x * x < 10)]
print(listcompr_04)

listcompr_05 = [x + y for x in '123' for y in '789']
print(listcompr_05)

distcompr_01 = {'name':'锤子','age':'23','ipone':'133'}
listcompr_06 = [x + y for x,y in distcompr_01.items()]
print(listcompr_06)
