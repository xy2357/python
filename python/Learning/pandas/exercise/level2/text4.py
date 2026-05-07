import pandas as pd

# df = pd.read_csv('property-data.csv')
# print(df.isnull())
# df = df.dropna(axis=0, how='any')
# print(df)

# data = {
#   "Date": ['2020/12/01', '2020/12/02' , '20201226'],
#   "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data)
# # df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# # date_check = pd.to_datetime(df['Date'], errors='coerce')
# # print(df[date_check.isna()]['Date'])
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df)

# person = {
#   "name": ['Google', 'Runoob' , 'Taobao'],
#   "age": [50, 40, 12345]    # 12345 年龄数据是错误的
# }
#
# df = pd.DataFrame(person)
#
# for x in df.index:
#     if df.loc[x, 'age'] > 120:
#         df.loc[x, 'age'] = 120
#
# print(df)

# person = {
#   "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
#   "age": [50, 40, 40, 23]
# }
#
# df = pd.DataFrame(person)
# df.drop_duplicates(inplace=True)
# print(df)
# data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
#
# df = pd.DataFrame(data)
#
# df_encoded = pd.get_dummies(df, columns=['City'])
# print(df_encoded)

# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 示例数据
# data = {
#     'Height': [150, 160, 170, 180, 190],
#     'Weight': [45, 55, 65, 75, 85],
#     'Age': [20, 25, 30, 35, 40]
# }
# df = pd.DataFrame(data)
# # 绘制相关性热图
# plt.figure(figsize=(8, 6))
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
# plt.title('Correlation Heatmap')
# plt.show()

data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}

df = pd.DataFrame(data)

grouped_multiple = df.groupby('Department').agg({'Salary': ['mean', 'sum']})
print(grouped_multiple[('Salary', 'mean')])