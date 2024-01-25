import pandas as pd
from datetime import datetime
import ast 
from warnings import simplefilter
simplefilter(action="ignore",category=FutureWarning)
# 读取csv文件，假设文件名为data.csv，分隔符为逗号
dataraw = pd.read_csv("animes.csv", sep=",")
# 删除第二列值重复的行，保留第一次出现的行，忽略第一行列名
data = dataraw.drop_duplicates(subset=dataraw.columns[1], keep="first", ignore_index=True)
tag_dict = {}
# 遍历第四列的每一行，假设第四列的列名为tags
for row in data["genre"]:
    # 将字符串转换为列表，去掉两边的中括号和引号，以逗号分隔
    tag_list = row.strip("[]").replace("'", "").split(",")
    # 遍历列表中的每一个tag
    for tag in tag_list:
        tag = tag.strip()
        # 如果tag已经在字典中，将其次数加一
        if tag in tag_dict:
            tag_dict[tag] += 1
        # 否则，将tag添加到字典中，初始次数为一
        else:
            tag_dict[tag] = 1
# 将字典转换为Dataframe，以tag和count为列名
tags = pd.DataFrame(tag_dict.items(), columns=["tag", "count"])
tags = tags[tags["tag"] != ""]
tags = tags.sort_values(by="count", ascending=False)
t10tags= tags.head(10)["tag"].to_dict()

def convert_to_standard_date(date_str):
    try:
        # 尝试将字符串解析为标准日期格式
        return datetime.strptime(date_str, '%Y/%m/%d').strftime('%Y/%m/%d')
    except ValueError:
        try:
            # 尝试将字符串解析为带日期的格式，如果只有年份和月份，则默认为1号
            return datetime.strptime(date_str, '%b %d, %Y').strftime('%Y/%m/%d')
        except ValueError:
            try:
                # 尝试将字符串解析为日期范围格式，只取 "to" 前面的部分作为日期
                start_date_str = date_str.split('to')[0].strip()
                return datetime.strptime(start_date_str, '%b %d, %Y').strftime('%Y/%m/%d')
            except ValueError:
                try:
                    # 尝试将字符串解析为只有年份的格式，设定为1月1号
                    return datetime.strptime(date_str + ' 1', '%Y %m').strftime('%Y/%m/%d')
                except ValueError:
                    try:
                        # 如果解析失败，说明是只有年份的格式，设定为1月1号
                        return datetime.strptime(date_str + ' 1', '%Y').strftime('%Y/%m/%d')
                    except ValueError:
                        # 如果仍然解析失败，删除对应的行
                        return pd.NaT
data['aired'] = data['aired'].apply(convert_to_standard_date)
data = data.dropna()
data = data.reset_index(drop=True)
data = data[data['aired'] >= '1993/01/01']
data = data.sort_values(by='aired')
time_dict = {}
tag_time=pd.DataFrame(index=tag_dict)
for index,row in data.iterrows():
    # 将字符串转换为列表，去掉两边的中括号和引号，以逗号分隔
    tag_list = row['genre'].strip("[]").replace("'", "").split(",")
    time = row['aired']
    if time in time_dict:
        time_dict[time] += 1
    else:
        time_dict[time] = 1
        tag_time[time] = 0
    # 遍历列表中的每一个tag
    for tag in tag_list:
        tag = tag.strip()
        tag_time.loc[tag,time] += 1
tag_time = tag_time.transpose()
shape = tag_time.shape

# 提取新列'sum'作为新的DataFrame
for i in range(1,shape[0]):
    tag_time.iloc[i,:] = tag_time.iloc[i,:] + tag_time.iloc[(i-1),:]
sum = tag_time.sum(axis=1)
selected_columns = list(t10tags.values())
tag_time = tag_time.loc[:, selected_columns]
#tag_time.to_csv('tagtime.csv')     
data.rename(columns={'uid': 'anime_id'}, inplace=True)
#data.to_csv("out.csv", index=False)
#tags.to_json('tags.json',orient='records')
ds= data.sort_values(by='popularity').head(10)[['title', 'members']]
ds=ds.set_index('title')
ds=ds.sort_values(by='members')
#ds.to_json('pop.json')
sum.to_json('sum.json')
print(sum)
