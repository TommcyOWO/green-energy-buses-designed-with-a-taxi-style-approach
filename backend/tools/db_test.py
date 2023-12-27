from pymongo import MongoClient
from collections import OrderedDict
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
wait = db.wait

result_dict = OrderedDict()

# 遍歷每條數據並進行統計
for data in wait.find():
    key = tuple(OrderedDict(data).items())[:-1]  # 忽略最後一個元素（"person"）
    if key not in result_dict:
        result_dict[key] = {"person": 0, **dict(data.items())}
    result_dict[key]["person"] += 1

# 將 ObjectId 轉換為字符串
for entry in result_dict.values():
    if '_id' in entry:
        entry['_id'] = str(entry['_id'])

# 將統計結果轉換為列表
result_list = list(result_dict.values())
result_json = json.dumps(result_list, ensure_ascii=False)
print(result_json)
