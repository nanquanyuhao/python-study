# keyword
# def sum(**kwargs):
#     """
#     kwargs 要放人的信息
#     你可以传
#     name
#     age
#     """
#     print(kwargs["name"])

# sum(name = "张三", age = 18)

def sum(name, age, **kwargs):
    print("name:", name)
    print("name:", age)
    print("name:", kwargs)

sum(name = "张三", age = 18, school = "尚硅谷", address = "北京市宏福科技园")