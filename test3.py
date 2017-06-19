'''
在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]

a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''



a = 10
def test():
    global a
    a = a + 1
    print(a)
test()


matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]


va = [[row[i] for row in matrix] for i in range(4)]
print(va)

a = []
for i in range(4):
     a.append([row[i] for row in matrix])

print(a)


b = []
for i in range(4):
     # the following 3 lines implement the nested listcomp
     transposed_row = []
     for row in matrix:
         transposed_row.append(row[i])
     b.append(transposed_row)

print(b)


import urllib
import urllib.request
import re

def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    #伪装浏览器
    request = urllib.request.Request(url,headers=headers) #构建请求
    response = urllib.request.urlopen(request) #获取服务器响应
    data = response.read() #读取图片
    return data
def get_image(data):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern,repr(data))
    num = 1
    for img in get_img:
        try:
            image = download_page(img)
            with open('F:\\pythonSpiderImg\{}.jpg'.format(num),'wb') as fp:
                fp.write(image)
                print('正在下载第{}张图片'.format(num).center(20,'='))
                num += 1
        except:
            print('href error')
            continue
    return

url = 'http://pic.yesky.com/451/106166451.shtml'
data = download_page(url)
get_image(data)


