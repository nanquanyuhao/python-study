# a = {1, 2, 3, 4, 1}
# 都是唯一的，不重复的
# print(a)

a = []
b = set()

print(type(b))

b.add(1)
b.add(2)
b.add(3)
b.add(1)

print(b)

b.remove(2)

print(b)

print(len(b))

print(2 in b)