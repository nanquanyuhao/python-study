my_list = [1, 2, 3, "three", 4.0, "five"]

# 访问列表中的单个元素
print(my_list[3])

my_list[0] = 100
print(my_list)

my_list.append("six")
print(my_list)

my_list.insert(1, "aaa")
print(my_list)

# del delete
del my_list[1]
print(my_list)

my_list = [100, 100, 2, 100, 100]
print(my_list)
# 从最左侧的元素开始删除
my_list.remove(100)
print(my_list)

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
print(my_list)
my_list.sort(reverse=True)
print(my_list)

# len() length
print(len(my_list))