#两种常用的排序操作

list_demo5a=list('printyour1940hans1')
print(list_demo5a)
b=list_demo5a
print(b)
list.sort(b)
print(list_demo5a)
print(b)#无论赋值与否，原地排序后，新列表和原列表都会改变顺序

list_demo5c=list('softtesting_technoligy')
print(list_demo5c)
d=list_demo5c
print(d)
sorted(list_demo5c)
print(list_demo5a)
print(d)
print(list_demo5c)#新序列与原序列不同
