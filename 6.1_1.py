#6.1_1

#冒泡排序
def BubbleSort(l):
    for i in range(0,len(l)):
        for j in range(i+1, len(l)):
            if(l[i]<l[j]):
                l[i],l[j] = l[j], l[i]

#快速排序              
def QuickSort(l, p, r):
    if p < r :
        x = l[p]
        i = p
        j = r
        while i < j :
            while i < j and l[j] < x :
                j -= 1
            if i < j :
                l[i] = l[j]
                i += 1
            while i < j and l[i] > x :
                i += 1
            if i < j :
                l[j] = l[i]
                j -= 1
        l[i] = x
        QuickSort(l, p, i-1)
        QuickSort(l, i+1, r)
    
    
if __name__ == '__main__':
    l = []
    while True:
        num = int(input("请输入一个正数 : "))
        if num == 0 :
            break
        l.append(num)
    #这里选择排序方式
    #BubbleSort(l)
    QuickSort(l, 0, len(l)-1)
    print("按成绩从高到低的排序的后结果为 : ")
    for i in l:
        print(i, end = " ")
