# def get_str():
#     return "a b c"

# print(get_str())

import random
# VSCode Pycharm
# 类型建议符
def get_one(c: str) -> str | set :
    print(c)
    a = ["a b c", {1, 2, 3}]
    a.remove({1, 2, 3})
    return random.choice(a)

get_one(123)
# 给公司写：能跑就行
# 给开源项目写代码：我怕丢人

# print(get_one().split(' '))