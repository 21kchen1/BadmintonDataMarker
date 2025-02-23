import logging
import os
import pandas as pd
from Resources.String import FileEndName

"""
    数据读取服务
    负责根据路径读取需要的所有数据
    @author chen
"""

class DataLoad:

    """
        设置字典，决定后续读取的数据类型
        @param modelDict 模型类型与实例字典
    """
    def __init__(self, modelDict: dict) -> None:
        self.modelDict = modelDict

    """
        获取路径中所有文件夹路径
        @param rootPath 文件夹路径
        @return list 路径列表
    """
    def getFilePaths(self, rootPath: str) -> list:
        filePaths = []

        for root, _, files in os.walk(rootPath):
            filePaths.extend([os.path.join(root, file) for file in files])

        return filePaths

    """
        根据字典载入数据
        @param rootPath 文件夹路径
        @return bool 是否读取成功
    """
    def loadData(self, rootPath: str) -> bool:
        # 获取所有文件路径
        filePaths = self.getFilePaths(rootPath)

        try:
            # 根据数据类型载入数据
            for key, dataModel in self.modelDict.items():
                for filePath in filePaths:
                    if not filePath.endswith(key + FileEndName.CSV):
                        continue
                    data = pd.read_csv(filePath)
                    # 读取除了第一列的数据
                    dataModel.loadData(*[data[column].values for column in data.columns[1:]])
        except Exception as e:
            logging.error(e)
            return False
        return True