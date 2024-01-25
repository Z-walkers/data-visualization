import pandas as pd
from datetime import datetime
import ast 
from warnings import simplefilter
simplefilter(action="ignore",category=FutureWarning)
average_df = pd.DataFrame(columns=['anime_id', 'Overall', 'Story', 'Animation', 'Sound', 'Character', 'Enjoyment'])
comment=pd.read_csv('out1.csv', na_values=['nan'])

# 进行其他数据清理操作，比如删除包含缺失值的行
new_df = comment.dropna()
# 将anime_id设置为索引，以便于后续的groupby操作
new_df.set_index('anime_id', inplace=True)

# 遍历每个动画ID，计算其各项评分的平均值
for anime_id, group_df in new_df.groupby(level=0):
    average_row = {
        'anime_id': anime_id,
        'Overall': group_df['Overall'].mean(),
        'Story': group_df['Story'].mean(),
        'Animation': group_df['Animation'].mean(),
        'Sound': group_df['Sound'].mean(),
        'Character': group_df['Character'].mean(),
        'Enjoyment': group_df['Enjoyment'].mean()
    }

    # 将平均评分添加到新的DataFrame中
    average_df = average_df.append(average_row, ignore_index=True)
data=pd.read_csv('out.csv', na_values=['nan'])
data['anime_id'] = data['anime_id'].astype(float)
result_df = pd.merge(average_df, data, on='anime_id', how='left')
result_df.to_csv("processed.csv",index=False)