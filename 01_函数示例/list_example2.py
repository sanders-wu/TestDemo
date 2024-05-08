#修改列表值，在列表中插入元素
list_demo=list('abcdefg')
print(list_demo)
list_demo.insert(-1,'P') #在列表元素之前插入元素
print(list_demo)
list_demo.append(['小米'])#在列表之后添加子列表
print(list_demo)
list_demo.extend('汽车')
print(list_demo)

