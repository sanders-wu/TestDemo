# #sort()对列表进行永久性排序—按字母排序
# names=['zhangsan','lisi','wangwu','zhaoliu']
# names.sort();
# print(names)
# names.sort(reverse = True)
# print(names)
#
# # 函数sorted()对列表进行临时排序—按字母排序
# color=['white','black','blue','red','green']
# b=sorted(color)
# print(b)
# print(color)
# # 函数sorted(),参数添加 reverse 对列表进行临时反转排序—按字母排序
# color=['white','black','blue','red','green']
# c=sorted(color,reverse=True)
# print(c)
# d=sorted((color))
# print(d)
#reverse()对列表进行反转排序—按元素排序,原列表元素已被永久修改,但是列表ID不变
color1=['white','yellow','blue','red','green']
print(id(color1))
color1.reverse()
# len()确定列表长度，即返回元素个数
print(len(color1))