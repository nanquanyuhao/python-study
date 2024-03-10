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

    # 很像默认方法
    def __call__(self):
        print("哈哈哈")

    def __len__(self):
        return len(self.name)

person = Person("小明", 20)

person()

print(len(person))