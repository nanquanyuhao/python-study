# 函数作用域，局部作用域
def my_func():
    x = 10
    print("函数内部打印：", x)
    for i in range(0, 10):
        print(i)
        for j in range(0, 5):
            print(j)
    print("!!!!!!!", i)
    print("!!!!!!!", j)

my_func()
print("函数外部打印：", x)