#多个变量赋值

#创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
a=b=c=1
print("a:",a)
print("b:",b)
print("c:",c)

#为多个对象指定多个变量
x,y,z = 1,2,"3"
print("x:",x)
print("y:",y)
print("z:"+z)


#String字符串
str = "Python"
# str[0] = "1" 字符串不可被改变
print(str)
print(str[0])
print(str[0:-1])
print(str[1:4])
print(str[-3:-1])
print(str[2:])
print(str*2)
print("hello "+str)
print("\n"+str)
print(r"\n"+str)#前面加r 使反斜杠不发生转义

#List 列表
list1 = [123,"abc",333,"bbbb"]
list2 = [555,"lplpk"]
print(list1)
print(list1[0])
print(list1[0:-1])
print(list1[1:3])
print(list1[1:])
print(list2*2)
print(list1+list2)
list1[1] = "-----"
print(list1)

#Tuple 元组
tuple1 = ("asdas",1234,"asfasfa","vcxb",252)
