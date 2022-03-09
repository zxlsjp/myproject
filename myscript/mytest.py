import os
dic = {'a': 1, 'b': 2}
print(f'first:{id(dic)}')
dic['a'] = 3
print(f'second:{id(dic)}')

def count_word():
    s='hello tank tank say hello sb sb'

    l=s.split()

    dic={}
    for item in l:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1
    print(dic)

def sum_self(x, y):
    """求和"""
    res = x+y
    print(res)


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

def filenum(path):
    if os.path.isfile(path):
        print(path)
        print('file num is 1 ')
        return
    num=0
    file_num=0
    for i in (os.listdir(path)):
        filepath=os.path.join(path,i)
        if os.path.isfile(filepath):
            num+=1
            print('文件是：%s'%filepath)
        else:
            print('当前目录%s'%filepath)
            file_num+=1
            filenum(filepath)
    print('当前文件数量:%s'%num,'当前文件夹数量%s'%file_num,'路径是:%s'%(path))

# path = '.'
def GetAllDeep(path):
    stack = []
    stack.append(path)
    # 处理栈，当栈为空时结束循环

    while len(stack) != 0:
        # 从栈里取出数据
        DirPath = stack.pop()
        # 目录下所有文件
        num = 0
        file_num = 0
        FileList = os.listdir(DirPath)
        # 循环处理每个文件
        for FileName in FileList:
            FileAbsPath = os.path.join(DirPath,FileName)
            if os.path.isfile(FileAbsPath) == True:
                print("是文件",FileAbsPath)
                num += 1
            else:
                # print("是目录",FileAbsPath)
                stack.append(FileAbsPath)
                file_num += 1
        print('当前文件数量:%s' % num, '当前文件夹数量%s' % file_num, '路径是:%s' % (FileAbsPath))



if __name__ == '__main__':
    #字典和字符串
    # sum_self(1, 2)  # 函数
    # count_word() # 运算
    # 类和对象
    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    # 文件处理：
    path='.'
    filenum(path)
    GetAllDeep(path)