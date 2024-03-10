class Person:

    # 构造方法
    def __init__(self, name, age):
        # self java js this
        # 指的是我们在构造的实例对象
        self.name = name
        self.age = age
        print("构造器被调用了")

    def say_hello(self):
        print(f"你好，我的名字是{self.name}，我今年{self.age}岁了")

xiao_ming = Person("小王", 18)
xiao_ming.say_hello()