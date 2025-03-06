import json
from typing import Union

"""
    JSON 自定义序列化逻辑
    @author chen
"""

"""
    json 编码器
    将字符串 list 还原
"""
class SingleLineArrayEncoder(json.JSONEncoder):
    def encode(self, obj) -> str:
        result = super().encode(obj)
        result = result.replace("'", '"').replace('"[', "[").replace(']"', "]").replace("\\", "")
        return result

"""
    递归转换 list
    将字典中所有 list 转换为 str
    @param data 需要转换的字典
    @return dict 转换完成的字典
"""
def dictListToStr(data: dict) -> Union[dict, str]:
    if isinstance(data, list):
        return str(data)
    if not isinstance(data, dict):
        return data
    for key, value in data.items():
        data[key] = dictListToStr(value)
    return data

"""
    紧凑数组编码
    json 中的数组将不会换行
    @param datas 列表或字典的 json
    @return str 编码完成的 json
"""
def compactArrayJson(datas: list) -> str:
    # 数据预处理
    if isinstance(datas, list):
        obj = [dictListToStr(data) for data in datas]
    elif isinstance(datas, dict):
        obj = dictListToStr(datas)
    # 编码
    return json.dumps(obj, cls= SingleLineArrayEncoder, ensure_ascii= False, indent= 4)