#'for'循环

schools = ['锤子','斧子','榔头']
for school in schools:
    print(school)

nsum = 0
for x in range(101): #'range'生成0-参数的数列，并顺序添加到'List'里面去,参数代表的的是列表长度，末尾值为"参数-1"
    nsum = nsum + x
print(nsum)

#'while'循环
#累加数值
nsum_while = 0
max_while = 100
while max_while > 0:
    nsum_while = nsum_while + max_while
    max_while = max_while - 1
print(nsum_while)

#'break'退出
nsum_break = 0
while nsum_break < 100:
    print(nsum_break)
    if nsum_break > 10:
        break #退出循环
    nsum_break = nsum_break + 1

#'continue'跳出

nsum_continue = 0
while nsum_continue < 10:
    if nsum_continue == 5:
        nsum_continue = nsum_continue + 1
        continue #跳出当前循环，进入下轮循环
    print(nsum_continue)
    nsum_continue = nsum_continue + 1