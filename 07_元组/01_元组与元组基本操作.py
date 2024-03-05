# 元组跟列表非常相似，不过元组是一个不可变的数据结构
my_tuple = (100, 200, 300)

print(my_tuple[0])

# my_tuple[0] = 400

# 下面方法编译器直接报错，元组不支持修改没有这个方法
# my_tuple.append(100)

print(len(my_tuple))