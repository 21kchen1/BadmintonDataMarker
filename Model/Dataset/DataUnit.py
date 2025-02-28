from Model.Dataset.Info import Info
from Model.Dataset.Label import Label

"""
    数据存储单元
    @author chen
"""

class DataUnit:
    """
        有效数据
        @param info 信息
        @param label 标签
        @param data 数据
        @param interData 插值数据
    """
    def __init__(self, info: Info, label: Label = None, data: dict = None, interData: dict = None) -> None:
        self.info = info.__dict__
        if label == None: self.label = label
        else: self.label = label.__dict__
        self.data = data
        self.interData = interData