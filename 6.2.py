#6.2

def BinarySearch(a, t):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = (h + l)//2
        if a[m] == t:
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
    if res == -1 :
        print("NO FOUND!")
    else:
        print(res)