# 0 - 100
# 使用循环，使用户可以多次猜测，直到猜对为止
# 如果用户猜中了，程序输出恭喜消息，并显示用户猜测的次数
# 如果用户输入的是命令"quit"，则退出游戏
# 如果用户输入的是命令"hint"，则程序会给出一个提示，告诉用户是否要继续猜大一点还是猜小一点
# 如果用户输入的是其他内容（非数字、非命令），则给出响应的错误提示，并让用户重新输入
# 记录用户的每次猜测，并在游戏结束后输出猜测历史

import random

# 先出来随机数，也就是实际的最终结果
num = random.randint(0, 100)

# 最终结果是猜对开始猜错
isTrue = False

# 存储猜测历史的数组
my_list = []
lastNum = 0

while not isTrue:
    score = input("请输入你猜的数字（0 - 100）\n")

    if score.isdigit():
        score = int(score)
        my_list.append(score)
        if num == score:
            isTrue = True
            print(f"恭喜您猜中结果为{num}，共猜了{len(my_list)}次，且猜测历史数据如下：")
            print(my_list)
            break
        else:
            print("不对")
        lastNum = score
    elif score == "quit":
        print("退出游戏")
        break
    elif score == "hint":
        if lastNum > num:
            print(f"上次猜的数是{lastNum}，需要小一些")
        else:
            print(f"上次猜的数是{lastNum}，需要大一些")
    else :
        my_list.append(score)
        print("用户的输入是不合法的，请重新输入")