# 这个程序 input 获取用户输入
# 判断用户输入的是不是纯数字，如果不是纯数字，那么就抛出异常

def check(input_value:str):
    # input str
    # isdigit 是不是纯数字
    if input_value.isdigit():
        print("用户给的是纯数字，nice")
    else:
        raise ValueError("用户输入的不是纯数字")
    
a = input("请输入一个纯数字")

check(a)