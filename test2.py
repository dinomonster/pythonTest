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
print("============字符串操作===============")
s = "Python"
# s[0] = "1" 字符串不可被改变
print(s)
print(s[0])
print(s[0:-1])
print(s[1:4])
print(s[-3:-1])
print(s[2:])
print(s*2)
print("hello "+s)
print("\n"+s)
print(r"\n"+s)#前面加r 使反斜杠不发生转义

#List 列表
print("============列表操作===============")
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
print("============元组操作===============")
tuple1 = ("asdas",1234,"asfasfa","vcxb",252)
tuple2 = ("cccc",888)
tuple3 = (list1,list2)
#tuple1[0] = "===" 元组不可变
print(tuple1)
print(tuple1[0])
print(tuple1[0:-1])
print(tuple1[1:3])
print(tuple1[1:])
print(tuple1*2)
print(tuple1+tuple2)
tuple3[0][0] = "111"#元组不可变，但是能包含可变的对象，比如list列表
print(tuple3)

#Set 集合 是一个无序不重复元素的序列。
print("============集合操作===============")
student = {"tom","jerry","wangwang","tom","Tom"}
print(student)
if('tom' in student):
	print("tom在集合中")
else:
	print("tom不在集合中")
a = set('tomasdasdf')
b = set('cvzafgsdfa')

print(a)
print(a-b)# a和b的差集
print(a|b)# a和b的并集
print(a&b)# a和b的交集
print(a^b)# a和b中不同时存在的元素

'''Dictionary 字典 列表是有序的对象结合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
'''
print("============字典操作===============")
dict = {} #注意{}创建一个空字典，创建空集合必须用set()
dict['aaa'] = "hello"
dict[2] = "world"
dict2 = {'name':'pengzhe','age':26}
print(dict)
print(dict['aaa'])
print(dict[2])
print(dict2.keys())
print(dict2.values())

dict2['age'] = str(dict2['age'])#类型转换
print(dict2.values())

