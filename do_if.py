#判断

is_if = False
if is_if: #'if'和'else','elif'后面加':'
    print('isTrue')
else:
    print('isFalse')

num_if = 500
if num_if < 50:
    print('max')
elif num_if < 1000: #'elif'为'else if'简写
    print('mid')
else:
    print('low')

if num_if: #'num_if'是非零数值、非空字符串、非空'list'等，就判断为'True'，否则为'False'
    print('yes')

#输入

put_str = input('put_str:') #'inptu'返回的数据类型为'str'
if put_str:
    print('not zero')
else:
    print('zero')