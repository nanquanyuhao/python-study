# 1 4 9 16 25

# x = []
# for i in range(1, 6):
#     x.append(i**2)

# 列表推导
# x = [i ** 2 for i in range(1, 6)]
# 新列表 = 【表达式 for 变量 in 可迭代对象 if 条件】

# y = [i for i in range(1, 11) if i % 2 == 0]

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

z = [[j for j in range(i, i + 3)] for i in range(1, 8, 3)]

print(z)