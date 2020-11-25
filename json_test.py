import pandas as pd
import json

df = pd.read_excel(r'C:\Users\jizeyuan\Desktop\短信分词\新建文件夹\短信JSON.xlsx', sheet_name='Sheet1')

dict_df = {}
dict_df['order_number'] = str(df['order_number'][0])
dict_df['sms'] = list( df['body'])

json_str = json.dumps(dict_df, ensure_ascii=False)

with open("json_str.txt", "w", encoding='utf-8') as f:
    f.write(json_str)

# print(df.to_json(orient='index',force_ascii=False))
