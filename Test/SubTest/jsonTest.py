# import json


# class SingleLineArrayEncoder(json.JSONEncoder):
#     def encode(self, obj):
#         result = super().encode(obj)
#         result = result.replace('"[', "[").replace(']"', "]").replace("\\", "")
#         return result


# def preprocess_data(data):
#     for value in data:
#         if "Label" in value:
#             value["Label"] = json.dumps(value["Label"])
#     return data


# # 假设 `data` 是你从原始 JSON 文件中加载的数据
# data = [
#     {"number": 50, "CategoryId": 0, "Label": [1, 1, 1, 0, 1]},
#     {"number": 48, "CategoryId": 27, "Label": [1, 1, 1, 0, 0]},
#     {"number": 48, "CategoryId": 22, "Label": [1, 0, 0, 0, 0]},
# ]

# # 预处理数据
# processed_data = preprocess_data(data)

# serialized_data = json.dumps(
#     processed_data, cls=SingleLineArrayEncoder, indent=4)

# file_path = "data.json"
# with open(file_path, "w", encoding="utf-8") as file:
#     json.dump(processed_data, file, cls=SingleLineArrayEncoder, ensure_ascii=False, indent=4)

import json

class SingleLineArrayEncoder(json.JSONEncoder):
    def encode(self, obj) -> str:
        result = super().encode(obj)
        result = result.replace("'", '"').replace('"[', "[").replace(']"', "]").replace("\\", "")
        return result

def strList(data: dict) -> dict:
    if isinstance(data, list):
        return str(data)
    if not isinstance(data, dict):
        return data
    for key, value in data.items():
        data[key] = strList(value)
    return data


# 定义 JSON 数据
datas = [
    {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "traveling", "coding"],
        "details": {
            "location": "New York",
            "skills": ["Python", "Data Science"]
        }
    }
]

with open("Large.json", "r", encoding="utf-8") as file:
    datas = json.load(file)

# 使用 json.dumps 序列化为 JSON 字符串
serialized_data = json.dumps([strList(data) for data in datas], cls=SingleLineArrayEncoder, indent=4)

file_path = "data.json"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(serialized_data)

with open(file_path, "r", encoding="utf-8") as file:
    datas = json.load(file)
    for data in datas:
        print(data["hobbies"][0 : 2])