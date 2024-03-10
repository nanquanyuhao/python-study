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

print(type(add))
aaaa = add

print(aaaa(2, 4))

calculator(subract, 5, 3)