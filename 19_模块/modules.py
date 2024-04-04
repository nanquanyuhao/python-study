# 函数的定义
# 类的定义
# 变量

def a():
    print("aaaaaaa")

def b():
    print("bbbbbbb")

hh = "hello world"

print("modules.py", __name__)

def add(a, b):
    return a + b

'''
__name__ 是一个特殊的变量，它在程序运行时被设置为当前模块（也就是当前的.py 文件）的名称。
当这个模块被直接运行时（即作为主程序运行），__name__ 的值就是 "__main__"。
通过检查 __name__ 是否等于 "__main__"，可以确定当前模块是作为主模块直接运行，还是被其他模块导入。
'''
if __name__ == "__main__":
    print(5 == add(2, 3))