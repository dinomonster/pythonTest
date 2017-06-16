print(123);

# input("\n\n按下 enter 键后退出")
x = "xxx";y="""三引号，
可以指定一个多行字符串"""
print("x:"+x)
print("y:"+y)
z = "这是一个带回车换行的字符串\n"
print(z)
zr = r"这是一个自然字符串\n"
print(zr)

#缩进相同的一组语句构成一个代码块，我们称之代码组。
#像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
#我们将首行及后面的代码组称为一个子句(clause)。
if (1+1==2):
    print(2)
elif (1+1==3):
    print(3)
else:
    print(4)

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print(x,end="")
print(y,end="")


#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *

#导入sys模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

#导入 sys 模块的 argv,path 成员
from sys import argv,path
print("==================Python from import===============")
# 因为已经导入path成员，所以此处引用时不需要加sys.path
print("path:",path)


'''
多行
注释
的写法
'''
