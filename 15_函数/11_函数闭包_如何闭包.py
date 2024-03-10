# def func():
#     y = 50
#     print(y)

# y = 100
# func()

def outer_func(x):
    def inner_func():
        print(x, y)
    return inner_func

y = 50

func1 = outer_func(19)
func1() # inner_func

func2 = outer_func(22)
func2() # inner_func

print(func1)
print(func2)