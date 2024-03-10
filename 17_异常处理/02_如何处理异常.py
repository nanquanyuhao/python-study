# try:
#     # 可能引发异常的代码块
#     ...
# except ExceptionType1:
#     # 处理 ExceptionType1 类型的异常
#     ...
# except ExceptionType2:
#     # 处理 ExceptionType2 类型的异常
#     ...
# else:
#     # 在没有异常发生时执行的代码块
#     ...
# finally:
#     # 无论是否发生异常，都会执行的代码块
#     ...

try:
    # "123" + 123
    a = [1, 2, 3]
    print(a[5])

except TypeError as e:
    print("发生了类型异常", e)
except IndexError as e:
    print("发生了列表下标越界异常")
else:
    print("一切安好！没有任何异常")
finally:
    print("无论如何，还是打印的")