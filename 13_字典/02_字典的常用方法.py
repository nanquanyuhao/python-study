# a = {
#     "name" : "小明",
#     "age" : 18,
#     "city" : "北京市"
# }
# None
# print(a.get("gender"))

# print(a["gender"])

# print(a.keys())

# for i in a.keys():
#     print(a[i])

# print(a.items())

# for k, v in a.items():
#     print(k, v)

a = {
    "name" : "小明",
    "age" : 18,
    "city" : "北京市"
}

# print("gender" in a)

# for i in a.values():
#     print(i)
# 3.6 之前的字典 key 是没有顺序的
# 但是从 3.6 （包括）之后 python 的 key 就有顺序了，这个顺序是我们添加键的顺序
print(len(a))