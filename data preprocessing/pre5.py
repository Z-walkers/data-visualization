import numpy as np
import pandas as pd

# 读取CSV文件到DataFrame
df = pd.read_csv('out.csv')

# 选取popularity和score两列
selected_columns = ['popularity', 'score']
new_df = df[selected_columns]
new_df = new_df.sort_values('score')
#new_df.set_index('popularity',inplace=True)
# 打印新的DataFrame
new_df.to_json('new.json',orient='records')