import json
import logging
import os

from Model.Dataset.DataUnit import DataUnit
from Resources.String import FileEndName, Encoding
from Util import Path

"""
    数据保存服务
    负责存储文件创建写入与删除
    @author chen
"""

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
        # 检测子文件 json 数量
        if not len([filePath for filePath in Path.getFilePaths(rootPath) if filePath.endswith(FileEndName.JSON)]) == 1:
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
        删除存储文件
        @return bool 是否删除成功
    """
    def deleteSave(self) -> bool:
        # 存储文件异常
        if not self.storePath or not os.path.exists(self.storePath):
            return False
        os.remove(self.storePath)
        return True

    """
        向存储文件尾部添加数据单元
        @param dataUnit 数据单元
    """
    def saveDataUnit(self, dataUnit: DataUnit) -> bool:
        # 存储路径异常
        if not self.storePath or not os.path.exists(self.storePath):
            return False

        try:
            # 读取数据
            with open(self.storePath, "r", newline= "", encoding= Encoding.UTF8) as file:
                dataSet = json.load(file)
            if not isinstance(dataSet, list):
                return False
            # 添加数据
            dataSet.append(dataUnit.__dict__)
            # 存储数据
            with open(self.storePath, "w", encoding= Encoding.UTF8) as file:
                json.dump(dataSet, file, ensure_ascii= False, indent= 4)
        except Exception as e:
            logging.error(e)
            return False
        return True

    """
        删除下标指定
    """