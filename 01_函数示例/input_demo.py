#input()的用法
#用户从终端输入
string_1=input("please enter your name:")
print("hi , nice to meet "+string_1)

#多行输入提示：
string_2=input('If you tell us who you are,we can personalize the message you see.')
string_2+="what's your first name"
print("\n",)

#判断体重
height = input("How tall are you ,in inches? ") #从键盘上输入的才算是input
print("显示输入数据类型：",type(height))
height = int(height) #输入的数据默认是字符串

if height >= 36:
   print("\n you're tall enought to ride")
else:
   print("\nyou'll be able to ride when you're a little older.")