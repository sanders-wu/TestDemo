#增加了注释
from random import choices


data=choices(range(1,10),k=20)
print(data)
data[:10]=sorted(data[:10])
data[10:]=sorted(data[10:],reverse=True)
print(data)
