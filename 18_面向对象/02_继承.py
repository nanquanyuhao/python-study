class Animal:

    def __init__(self, name) :
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现我这个方法")
    
class Dog(Animal):

    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    pass

dog = Dog("小白")
dog.speak()

cat = Cat("小花")
cat.speak()