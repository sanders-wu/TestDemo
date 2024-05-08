#列表基本操作
colours=["red","blue","black"]
print(colours) #打印输出结果
print(type(colours)) #打印变量数据类型

testing1=list('testing')
print(testing1) #使用内置函数list创建列表
print(type(list))

testing2=['123','erting',['spring','summer']]
print(testing2[0],testing2[-1],testing2[2][0],testing2[2][1],testing2[-1][-1],testing2[-1][-2])
print(testing2[-1][0],testing2[-1][1])

del colours
del testing1
del testing2[2][0]
print(testing2)
del testing2