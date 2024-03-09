# a, b, c = (1, 2, 3)
# 拆包就是把元组或者列表里的元素拿出来给变量
# print(a)
# print(b)
# print(c)

# a, b, c = [4, 5, 6]
# print(a)
# print(b)
# print(c)

# a, b, c = 2, 3, 4
# print(a)
# print(b)
# print(c)

# a, b, c, d, e = (1, 2, 3, 4, 5)

# print(a)
# print(b)
# print(c)

# *a, b, c, d = (1, 2, 3, 4, 5)

# print(a)
# print(b)
# print(c)

# [*a] = (1, 2, 3)

# print(a)

# (a, b, c) = 1, 2, 3

# print(a)
# print(b)
# print(c)

(a, b, (c, d)) = 1, 2, [3, 4]
print(a)
print(b)
print(c)
print(d)