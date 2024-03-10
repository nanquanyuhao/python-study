# print(1, 2, 3, 4)

a = [1, 2, 3, 4]
# print(a)
# print(a[0], a[1], a[2], a[3])
# print(*[1, 2, 3, 4])
# print(1, 2, 3, 4)

# def sum(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total += num
#     return total

# a = [1, 2, 3, 4, 5, 6]

# print(sum(*a))

def add(a, b):
    print(a + b)

a = [1, 2]
add(*a)
# add(1, 2)

################################################
def print_info(name, age):
    print("名字是：", name)
    print("年龄是：", age)

a = {
    "age" : 19,
    "name" : "小王"
}

print_info(**a)