#python字符串格式化输出：

name='xiaoming'
age=13 #{}中直接使用变量
print(f'My name is {name},My age is {age}') #{}中运行表达式
print(f'{1+2+3}')#调用Python内置函数
print(f'{name.upper()}')#用lambda匿名函数：可以做复杂的数值计算
fun = lambda x : x+1
print(f'{fun(age)}')#输出格式不一致

'''format是python2.6新增的一个格式化字符串的方法,相比%格式化方法有如下优点：
单个参数可以多次输出，参数顺序可以不相同
填充方式十分灵活，对齐方式十分强大
官方推荐用的方式
'''
#


'''print("...{索引}, ... , {索引}, ...".format(值1, 值2))
#索引{}为空，默认按照顺序取值
print("...{key1}, ... , {key2}, ...".format(key1=value,key2=value))
'''
name='xiaoming'
age=12
print('My name is {}, My age is {}'.format(name,age))
print('My name is {0}, My age is {1}'.format(name,age))
print('My name is {name}, My age is {age}'.format(name='xiaoming',age=12))
#输出：My name is xiaoming,My age is 12

'''format进阶 填充对齐
'''
# 先取到值,然后在冒号后设定填充格式：{索引:[填充字符][对齐方式][宽度]}

# *<20：左对齐，总共20个字符，不够的用*号填充

print('{0:*<20}'.format('hellopython'))

# *>20：右对齐，总共20个字符，不够的用*号填充

print('{0:*>20}'.format('hellopython'))

# *^20：居中显示，总共20个字符，不够的用*号填充

print('{0:*^20}'.format('hellopython'))

'''f-string格式化
在Python 3.6中引入 了f-strings，不仅比str.format使用简单，而且效率也更高。
'''

#f-string是字符串前面加上 "f"，{}直接使用变量、表达式等。
print(f'My name is {name},My age is {age}')   #{}中运行表达式
print(f'{1+2+3}')   #调用Python内置函数
print(f'{name.upper()}')   #用lambda匿名函数：可以做复杂的数值计算
fun = lambda x : x+1
print(f'{fun(age)}')
