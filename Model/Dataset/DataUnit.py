from Model.Dataset.Info import Info
from Model.Dataset.Label import Label

"""
    数据存储单元
    @author chen
"""

class DataUnit:
    """
        @param info 信息
        @param label 标签
        @param data 数据
    """
    def __init__(self, info: Info, label: Label, data: dict) -> None:
        self.info = info
        self.label = label
        self.data = data