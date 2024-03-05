# str int float bool
num = 3.74
num_int = int(num)
# print(num_int)

# int 转 float
num_int = 3
num_float = float(num_int)
# print(type(num_float))

# int/float 和 str 进行转换
num_int = 123
num_float = 3.14
# str
str_int = str(num_int)
str_float = str(num_float)

# java 等语言中可以如此处理，但是 Python 中必须转为明确的字符串
str2 = "hello" + str(num_int)

# print(str_int)
# print(num_float)

# str 转成数值类型
str_int = "1234"
str_float = "3.14"
# int() float()
num_int = int(str_int)
num_float = float(str_float)
# print(type(num_int))
# print(type(num_float))

# bool str 互相转化
# str 转 bool
str1 = "13452345334"

bool1 = bool(str1)

# print(bool1)

bool_true = True
bool_false = False

str_1 = str(bool_true)
str_2 = str(bool_false)

# print(str_1)
# print(type(str_1))
# print(str_2)
# print(type(str_2))

# int/float 和 bool 转换

num_zero = -1
num_float_zero = -2.0

bool1 = bool(num_zero)
bool2 = bool(num_float_zero)


bool_true = True
bool_false = False

int_true = int(bool_true)
int_false = int(bool_false)
float_true = float(bool_true)
float_false = float(bool_false)

print(float_true)
print(float_false)