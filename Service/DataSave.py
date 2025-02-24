
"""
    数据保存服务
    @author chen
"""

import json
import logging
import os

from Resources.String import FileEndName, Encoding


class DataSave:

    """
        数据集创建，单元保存与删除
    """
    def __init__(self) -> None:
        self.storePath = None

    """
        检测路径能否生成数据集
        @param rootPath 路径
        @return bool 是否能
    """
    def checkPath(self, rootPath: str) -> bool:
        # 路径本身是否存在
        if not os.path.exists(rootPath):
            return False
        # 检测路径同级文件是否存在 json
        if os.path.exists(rootPath + FileEndName.JSON):
            return False
        return True

    """
        创建存储文件
        @param rootPath 路径
        @return bool 创建成功
    """
    def createSave(self, rootPath: str) -> bool:
        if not self.checkPath(rootPath):
            return False
        # 存储路径
        self.storePath = rootPath + FileEndName.JSON
        # 以数组形式存储数据
        with open(self.storePath, "w", newline= "", encoding= Encoding.UTF8) as file:
            json.dump([], file, ensure_ascii= False, indent= 4)
        return True

    """
        向存储文件尾部添加数据单元
        @param dataUnit 数据单元 dict
    """
    def saveDataUnit(self, dataUnit: dict) -> bool:
        # 存储路径异常
        if not self.storePath or not os.path.exists(self.storePath):
            return False

        # 读取数据
        try:
            with open(self.storePath, "r", newline= "", encoding= Encoding.UTF8) as file:
                dataSet = json.load(file)
        except Exception as e:
            logging.error(e)
            return False

        if not isinstance(dataSet, list):
            return False
        # 添加数据
        dataSet.append(dataUnit)
        # 存储数据
        with open(self.storePath, "w", encoding= Encoding.UTF8) as file:
            json.dump(dataSet, file, ensure_ascii= False, indent= 4)
        return True