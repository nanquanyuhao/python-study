# input

# 控制台会等待在此行等待输入
x = input("请输入你的年龄\n")
print("123")
print(type(x))

if x.isdigit() :
    print("用户的输入是合法的")
    if int(x) > 35 :
        print("恭喜你35岁了")
else :
    print("用户输入的不是数字")