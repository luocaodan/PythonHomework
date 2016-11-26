#6.1_2

class Student:
    def __init__(self, name, score, math):
        self.name = name
        self.score = score
        self.math = math
    
    #这个可以直接实现类的比较
    #例如：classname1 < classname2
    def __lt__(self, other):
        if self.score < other.score:
            return 1
        elif self.score == other.score and self.math < other.math:
            return 1
        else:
            return 0
    
    #实现类的打印，print时会调用这个方法
    #例如：print(类名)
    def __repr__(self):
        return self.name


def sort(l):
    for i in range(len(l)-1):
        min = i
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]
    return l


#插入排序
def insert_sort(lst):
    n=len(lst)
    if n==1: return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]: lst[j],lst[j-1]=lst[j-1],lst[j]
        print(lst)
    return lst


if __name__ == "__main__":
    stu_list = []
    while 1:
        name = input("请输入姓名:")
        if name == '':
            break
        score = int(input("请输入总成绩:"))
        math = int(input("请输入数学成绩:"))
        stu_list.append(Student(name, score, math))
    stu_list = sort(stu_list)
    print("按成绩从高到低的排序的后结果为 : ")
    for i in stu_list:
        print(i, end = " ")
