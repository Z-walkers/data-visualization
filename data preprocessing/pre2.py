import pandas as pd
from datetime import datetime
import ast 
from warnings import simplefilter
simplefilter(action="ignore",category=FutureWarning)
comment=pd.read_csv('reviews.csv', na_values=['nan'])

# 进行其他数据清理操作，比如删除包含缺失值的行
comment = comment.dropna()
new_columns = ['anime_id', 'Overall', 'Story', 'Animation', 'Sound', 'Character', 'Enjoyment']
new_df = pd.DataFrame(columns=new_columns)

# 遍历原始DataFrame的每一行
for index, row in comment.iterrows():
    anime_id = row[2]  # 假设编号在第二列
    ratings_str = row[5]  # 假设评分字符串在第六列

    # 将评分字符串转换为字典
    ratings_dict = ast.literal_eval(ratings_str)

    # 创建新的行数据
    new_row = {'anime_id': anime_id}
    new_row.update(ratings_dict)

    # 将新的行数据添加到新的DataFrame中
    new_df = new_df.append(new_row, ignore_index=True)
'''

'''
new_df.to_csv("out1.csv", index=False)