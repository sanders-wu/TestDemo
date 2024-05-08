#作为函数的返回值
#function3=lambda x,y:x*x+y*y

def foo4(x,y):
    return lambda:x+y

print(foo4(4,6))