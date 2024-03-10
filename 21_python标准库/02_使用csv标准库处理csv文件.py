import csv

data = [
    {
        "姓名" : "张三",
        "年龄" : 25,
        "城市" : "北京"
    },
        {
        "姓名" : "李四",
        "年龄" : 30,
        "城市" : "上海"
    },
        {
        "姓名" : "王五",
        "年龄" : 28,
        "城市" : "广州"
    }
]

# 姓名，年龄，城市
# "张三", 25, "北京"
# "李四", 30, "上海"
# "王五", 28, "广州"

# with open("data.csv", 'w', newline = '', encoding = "utf8") as csvfile:
#     header = ["姓名", "年龄", "城市"]
#     writer = csv.DictWriter(csvfile, fieldnames = header)
#     writer.writeheader()
#     writer.writerows(data)

with open('data.csv', 'r', newline = '', encoding = "utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)