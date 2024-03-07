# for 变量 in 序列：
    # 代码块

a_list = [1, 3, 2, "abc"]

# 我们没有办法知道 元素是列表里的第几个
# for i in a_list:
#     print(i)

# enumerate，获取的 i 是整数类型
# for i, item in enumerate(a_list):
#     print(i, item, sep = "--", end = "\t")

a_list = [1, 3, 2, "abc"]
b_list = [2, 3, 1, "bbb"]

# for i in range(len(a_list)):
#    print(a_list[i], b_list[i])

# zip
for i, j in zip(a_list, b_list):
    print(i, j)