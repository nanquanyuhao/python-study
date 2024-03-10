# js 对象
# c / go struct
# java map
# python dict（字典）
# 键 : 值 （键值对）字典里就是一堆的键值对
# key : value (kv)
# map（映射）
# a = {
#     "小明" : 13,
#     "小王" : 23
# }

# print(a["小明"])
# a = {
#     1.1 : 13,
#     2 : 23
# }
# print(a[1.1])

# 哈希值 散列值
# a = {
#     [2, 3, 4] : 13,
#     2 : 23
# }
# print(a[[2, 3, 4]])
# 不可变的数据类型 才是可hash的 元组 整数 浮点数 字符串
# a = {
#     1 : 13,
#     1 : 23
# }
# print(a[1])

# print(a.keys())
# a = [1, 2]
# b = [1, 2, 3]

# c = {
#     a : "123", # [1, 2]
#     b : "245"
# }
# a.append(3) # 引用

# a = [1, 2, 3]
# b = a
# print(b)
# a.append("hello")
# print("a:", a)
# print("b:", b)

a = {
    "name" : "小王",
    "age" : 17,
    "school" : {
        "name" : "尚硅谷",
        "address" : "北京市宏福科技园"
    }
}

# print(a["school"]["name"])
print(a)
# a["name"] = "小李"
a["gender"] = "女"
del a["age"]
print(a)