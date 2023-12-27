from pymongo import MongoClient
from collections import OrderedDict
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
wait = db.wait

result_dict = OrderedDict()

# 遍歷每條數據並進行統計
for data in wait.find():
    key = (data["origins"], data["destination"])  # 使用元組作為鍵
    if key not in result_dict:
        result_dict[key] = {"_id": [], "origins": data["origins"],
                            "destination": data["destination"], "users": []}
    result_dict[key]["_id"].append(str(data["_id"]))
    result_dict[key]["users"].append(data["username"])

# 將統計結果轉換為列表
result_list = list(result_dict.values())
result_json = json.dumps(result_list, ensure_ascii=False)
print(result_json)
