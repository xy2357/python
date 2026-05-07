import json

import pandas as pd
import numpy as np
from glom import glom

pd.set_option('display.max_columns', None)
# df = pd.read_csv('nba.csv')
# print(df.to_string(index=False))

# df = pd.read_excel('ImpactConfig.xlsm', sheet_name='Buff', skiprows=range(1,6), index_col=0, nrows=110, engine = 'openpyxl')
# df = pd.read_excel(
#     'ImpactConfig.xlsm',
#     sheet_name='Buff',
#     skiprows=range(1, 6),
#     index_col=0,
#     nrows=110,
#     engine='openpyxl'
# )
#
# print(df)

# df = pd.read_json('nested_list.json')
#
# print(df)

# with open('nested_list.json', 'r') as f:
#     data = json.loads(f.read())
#
# df_nested_list = pd.json_normalize(data, record_path=['students'], meta=['class', 'school_name'])
# print(df_nested_list)
#
# data = [
#  {
#    "state": "Florida",
#    "shortname": "FL",
#    "info": {"governor": "Rick Scott"},
#    "counties": [
#      {"name": "Dade", "population": 12345},
#      {"name": "Broward", "population": 40000},
#      {"name": "Palm Beach", "population": 60000}
#    ]
#  },
#  {
#    "state": "Ohio",
#    "shortname": "OH",
#    "info": {"governor": "John Kasich"},
#    "counties": [
#      {"name": "Summit", "population": 1234},
#      {"name": "Cuyahoga", "population": 1337}
#    ]
#  }
# ]

# result = pd.json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
# print(result)

# with open('nested_mix.json', 'r') as f:
#     data = json.loads(f.read())
#
# df_nested_mix = pd.json_normalize(data, record_path='students', meta=['school_name', 'class', ['info', 'president'], ['info', 'contacts', 'email']])
# print(df_nested_mix)

# with open('nested_deep.json', 'r') as f:
#     data = json.loads(f.read())
#
# df_nested_deep = pd.json_normalize()

df = pd.read_json('nested_deep.json')

# print(df.loc[0,['students']].grade)
data = df['students'].apply(lambda x: glom(x, 'id'))
print(data)