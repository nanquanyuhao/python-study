# 匿名函数
# 加法
def add(a, b):
    return a + b

# 减法
def subract(a, b):
    return a - b

# 计算
def calculator(one_function, a, b):
    result = one_function(a, b)
    print("计算结果：", result)

calculator(add, 5, 3)
# 乘法
calculator(lambda a, b : a * b, 5, 3)

abc = lambda a, b : a * b
# print(type(abc))

print(abc(10, 100))