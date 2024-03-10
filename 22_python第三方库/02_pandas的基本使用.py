import pandas as pd

# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

df = pd.read_csv('pandas_data.csv')

print(df)

# 求平均值
print(df['age'].mean())
print(df['age'].max())

# 筛选出 city 是否为 New York 的数据
print(df[df['city'] != "New York"])