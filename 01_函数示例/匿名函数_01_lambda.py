# 匿名函数赋值给一个变量，用变量来调用该函数：
function1=lambda x:x+1
print(function1(10))

#与如下函数功能相同
def fuction2(x):
    x=x+1
    return x
fuction2(10)
