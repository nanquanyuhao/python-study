# 拆包（解包）
# def sum(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total += num
#     return total

# print(sum(1, 2, 3, 4, 5, 6))

# def sum(a, b, *args):
#     print("a:", a)
#     print("b:", b)
#     print(args)

# print(sum(1, 2, 3, 4, 5, 6))

def sum(a, *args, b):
    print("a:", a)
    print("b:", b)
    print(args)

print(sum(1, 2, 3, 4, 5, 6))

a, *args, b = 1, 2, 3, 4, 5, 6

# print("a:", a)
# print("b:", b)
# print(args)

def sum(a, b, *args):
    print("a:", a)
    print("b:", b)
    print(args)