name = "Alice"
age = 18
print(f"我的名字是{name}，我的年龄是{age}")
print("我的名字是{}，我的年龄是{}".format(name, age))

print("a\tb")
# 原始字符串就是禁用掉转义功能
print(r"a\tb")
# 禁用了转义还被单引号引用起来
print(repr("a\tb"))