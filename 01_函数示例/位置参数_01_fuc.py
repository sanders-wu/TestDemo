#按照位置顺序传递参数值
def function1(argu1,argu2,argu3):
    return

n1=1
n2=2
n3=3

help(function1)
function1("number1","number2","number3")
function1(100,argu3=90,argu2=30)
m1=3
m2=4
function1(m1,argu3=900,argu2=m2)
function1(n1,n2,n3)
#参数个数不一致，报错
function1(100,200)

function1(100,200,300,500)


