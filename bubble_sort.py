#coding= utf-8
import random
#定义三个常量用来表示下限、上限和数组长度
start = 1
stop = 100
length = 100
#定义一个新数组存放随机数
list = []
def random_list(start, stop, length):
    for i in range(length):
        list.append(random.randint(start, stop))  #把生成的随机数出入到list
    return list

print("随机生成的数组为：")
print(random_list(start,stop,length))

i = 5
for i in range(len(list) - 1):   #循环次数 n - 2 次
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            #list[j],list[j + 1] = list[j + i],list[j]  #元组的方式
            tmp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = tmp
print("排序后的数组为：")
print(list)
