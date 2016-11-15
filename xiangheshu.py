# 5-1.py
# 不需要输入


def get_num(x):
    """
    获得因数和
    :param x:输入目标数
    :return:因数和
    """
    num_sum = 1
    for i in range(2, int(x**0.5 + 1)):
        if x % i == 0:
            num_sum += i
            num_sum += x // i
    return num_sum

if __name__ == "__main__":
    for a in range(1000, 10000):
        # 设b为a的所有因数和
        b = get_num(a)
        # 求出b的所有因数和
        sum_b = get_num(b)

        # 判断b的因数和与a是否相等并输出结果
        if a == sum_b:
            print(a, b)
