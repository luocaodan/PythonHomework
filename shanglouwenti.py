# 5-3.py


# 定义函数
def up_stairs(i):
    """
    :param i:当前台阶数
    :return:当前方法数
    """
    if i == 3:
        return 4
    if i == 2:
        return 2
    if i == 1:
        return 1

    # 读取全局变量
    global count
    # 容易写出递归式 f(n) = f(n - 1) + f(n - 2) + f(n - 3)
    count = up_stairs(i - 1) + \
        up_stairs(i - 2) + \
        up_stairs(i - 3)
    return count

# 主程序
if __name__ == '__main__':
    # 输入台阶数
    n = int(input("How many steps:"))
    count = 0
    # 调用函数
    up_stairs(n)
    print("There are", count, "solutions.")

