# 编写一个 Python 程序，要求用户输入一个分数，并将其存储在变量 score 中。
# 检查输入的分数是否为数字，并且是否在有效的范围内（0到100之间）。如果输入的分数无效，输出一条错误消息，提示用户重新输入。
# 如果输入的分数有效，则使用条件语句对其进行评估，输出该分数对应的等级：
# 分数在 90 分以上，对应的等级为 A；
# 分数在 80 分以上 90 分一下，对应的等级为 B；
# 分数在 70 分以上 80 分一下，对应的等级为 C；
# 分数在 60 分以上 70 分一下，对应的等级为 D；
# 分数低于 60 分，对应的等级为 E。

score = input("请输入你的分数\n")

if score.isdigit() :
    if int(score) >= 0 :
        if int(score) <= 100 :
            if int(score) > 90 :
                print("等级为 A")
            elif int(score) > 80 :
                print("等级为 B")
            elif int(score) > 70 :
                print("等级为 C")
            elif int(score) > 60 :
                print("等级为 D")
            else :
                print("等级为 E")
        else :
            print("用户的输入是不合法的，请重新输入")
    else :
        print("用户的输入是不合法的，请重新输入")