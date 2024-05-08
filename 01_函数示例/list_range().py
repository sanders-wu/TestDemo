#函数range()的常见用法：
#生成一系列的数字
import random
for num in range(-2,9,2): #从指定的第一个值开始到达指定的第二个值后停止
    print(num)

#创建仅有数值元素的列表
list_num=list(range(1,20))
print(list_num)
list_num=list(range(1,20,2))
print(list_num)

list_num=[]
numbers=range(1,11)
for num in numbers:
    list_num.append(num*num)
print(list_num)
#最小值，最大值，求和计算
min_number=min(list_num)
max_number=max(list_num)
sum_number=sum(list_num)
print(min_number+max_number,sum_number)


