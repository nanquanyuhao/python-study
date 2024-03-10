# define
def add(a, b):
    """
    这个函数就是把两个参数的和打印出来
    并且返回这个和
    """
    c = a + b
    print("函数内部打印", c)
    return  c

x = add(1, 2)
print("调用结果",x)