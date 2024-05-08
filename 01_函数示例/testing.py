'''
列表
'''
#创建列表
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#访问列表元素
a=bicycles[0]
b=bicycles[-1]
print(a,b)
#修改列表元素
names=['zhangsan','lisi','wangwu','zhaoliu']
print(names)
names[1]='lidan'
print(names)
#在列表中添加元素
names=[]
print(names)
names.append('chenqi')
print(names)
names.append('chenba')
print(names)
# 在列表中删除元素的两种方式：
'''
如果你要从列表中删除的一个元素，且不再以任何方式使用它，就使用del语句；
如果你要在删除元素后还能继续使用它，就使用方法pop()
'''
#方式一：根据索引删除指定的元素
names=['zhangsan','lisi','wangwu','zhaoliu']
del  names[1]
print(names)
#方式二：删除最后一个元素
names=['zhangsan','lisi','wangwu','zhaoliu']
poped_names=names.pop()
print(poped_names)
print(names)
print('the be delted  name is '+poped_names+'.')
print('the first  name is '+poped_names.title()+'.')
# 方式三：根据值删除元素
names=['zhangsan','lisi','wangwu','zhaoliu']
names.remove('lisi')
print(names)
