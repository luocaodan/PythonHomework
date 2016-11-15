# 5-2.py


# 定义函数
def func(name_list, start_with, count, direction):
    """
    :param name_list:目的列表
    :param start_with:开始索引
    :param count:出局时数的数
    :param direction:1代表顺时针，0代表逆时针
   """
    if len(name_list) == 1:
        print(name_list[0])
        return
    p = start_with
    if direction:
        p = (p + count - 1) % len(name_list)
        print(name_list[p])
        del name_list[p]
        start_with = p - 1
    else:
        p = (p - count + 1) % len(name_list)
        print(name_list[p])
        del name_list[p]
        start_with = p
    # 对direction取反
    direction = not direction

    # 递归调用
    func(name_list, start_with, count, direction)

if __name__ == "__main__":
    # 输入总人数n，开始号码a，每次出局的号码m
    n = int(input("输入总人数:"))
    a = int(input("输入开始号码:"))
    m = int(input("输入每次出局号码:"))

    # 生成号码列表
    nameList = list(range(1, n+1))
    # 调用函数
    func(nameList, a - 1, m, 1)
