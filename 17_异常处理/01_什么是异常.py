# " abc" + 123

def func1():
    "abc" + 123

def func2():
    print("我是func2，我被调用了")
    func1()

print("程序开始运行了")
func2()

# Python 中有许多内置的异常类型，以下是一些常见的异常类型：
# ZeroDivisionError: 除以零错误
# TypeError: 类型错误，例如将不兼容的类型进行操作
# ValueError: 值错误，例如将无效的值传递给函数
# FileNotFoundError: 文件不存在错误，当尝试打开不存在的文件时引发
# IndexError: 索引错误，当访问列表、元组或字符串中不存在的索引时引发
# KeyError: 键错误，当在字典中使用不存在的键时引发
# NameError: 名称错误，当使用未定义的变量或函数名时引发
# AttributeError: 属性错误，当访问不存在的属性或方法时引发
# ImportError: 导入错误，当导入模块失败时引发
# IOError: 输入/输出错误，发生文件操作错误时引发
# PermissionError: 权限错误，当尝试执行没有权限的操作时引发
# KeyboardInterrupt: 键盘中断错误，当用户中断程序执行时引发
# 这只是一些常见的异常类型，实际上 Python 还提供了更多的异常类型，你可以在 Python 官方文档中找到完整的异常类型列表