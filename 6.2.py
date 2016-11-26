#6.2
#二分搜索
def BinarySearch(a, t):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = (h + l)//2
        if a[m] == t:
            #位置是从1开始的，下标是从0开始
            return m+1
        elif a[m] < t :
            l = m + 1
        else:
            h = m - 1
    return -1

if __name__ == "__main__":
    ele = int(input("请输入一个数 : "))
    a=[1,2,3,5,7,9]
    res = BinarySearch(a,ele)
    #判断返回的值，若果是-1意味着没找到
    if res == -1 :
        print("NO FOUND!")
    else:
        print(res)