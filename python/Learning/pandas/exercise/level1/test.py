import pandas as pd

pd.set_option('display.float_format', '{:.0f}'.format)

df1 = pd.read_csv('20260423_035018_17033_gue4e.csv')
df2 = pd.read_csv('20260423_034855_16931_gue4e.csv')

df1['flag'] = df1['properties_stage_id'] > 40010999
user = (df1.groupby(['b_role_id', 'b_zone_id', 'flag']))['properties_stage_id'].max().unstack().rename(columns={False: '塔1',True: '塔2'}).astype('Int64')

print(user)