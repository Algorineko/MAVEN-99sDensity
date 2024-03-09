# 移除缺失数据
import pandas as pd

column_names = [
    'Orbit N0.',
    'Time of Event (UTC)',
    'Time of Apoapsis UTC',
    'Solar Longitude',
    'Solar Latitude',
    'Spacecraft Longitude',
    'Spacecraft Latitude', 
    'Altitude',
    'Solar Distance',
    'Martian Year',
    'Ls', 'Event',
    'Notes'
]
# 创建一个包含所有列名的列表，用于parse_dates参数
date_columns = ['Time of Event (UTC)', 'Time of Apoapsis UTC']
# 读取CSV文件，指定列名和日期时间列
df = pd.read_csv('data/Mission_Timeline_delivery 1-34.csv', names=column_names, parse_dates=date_columns)
print(df.columns)
# 处理缺失值
df = df.dropna(subset=['Solar Longitude', 'Solar Latitude', 'Spacecraft Longitude', 'Spacecraft Latitude', 'Altitude'])

df.to_csv('rawData/processed_data.csv', index=False)