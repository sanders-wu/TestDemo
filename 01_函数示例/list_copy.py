#切片，使用列表的一部分
list_names=['zhangsan','lisi','wangwu','zhaoliu']
print(list_names[0:3]) # 前一个数从索引0开始，后一个数截止到索引3(第4个元素)但不包括索引3
print(list_names[2:3]) # 前一个数从索引2开始，后一个数截止到索引3不包括索引3
print(list_names[2:]) # 前一个数从索引2开始，后一个数截止到末尾
print(list_names[:2]) # 前一个数从索引0开始，后一个数截止到索引2不包括索引2
print(list_names[:]) # 前一个数从索引0开始，后一个数截止到到末尾，即复制生成一个新列表
print(list_names[:-2])  # 前一个数从索引0开始，后一个数截止到索引-2不包括索引-2
print(list_names[-2:])  # 前一个数从索引-2开始，后一个数截止到末尾

#遍历切片
for number in list_names[0:-1]:
    print(number.title())
    print(number)
#根据切片的一个特性，复制列表并生成一个新的列表：
list_names=['zhangsan','lisi','wangwu','zhaoliu']
list_names2=list_names
list_names1=list_names[:]
print(id(list_names))
print(id(list_names1))
print(id(list_names2))
