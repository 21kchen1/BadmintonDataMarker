import json
import logging
import pandas as pd
from Model.Note.Note import Note
from Resources.String import FileEndName
from Util import Path

"""
    数据读取服务
    负责根据路径读取需要的所有数据
    @author chen
"""

class DataLoad:

    """
        设置字典，决定后续读取的数据类型
        @param modelDict 模型类型与实例字典
        @param note 数据基本信息
    """
    def __init__(self, modelDict: dict, note: Note) -> None:
        self.modelDict = modelDict
        self.note = note

    """
        根据字典载入数据
        @param rootPath 文件夹路径
        @return bool 是否读取成功
    """
    def loadData(self, rootPath: str) -> bool:
        # 获取所有文件路径
        filePaths = Path.getFilePaths(rootPath)

        try:
            # 根据数据类型载入数据
            for key, dataModel in self.modelDict.items():
                # 重置数据模型
                dataModel.cleanData()
                for filePath in filePaths:
                    if not filePath.endswith(key + FileEndName.CSV):
                        continue
                    data = pd.read_csv(filePath)
                    # 读取除了第一列的数据
                    dataModel.loadData(*[data[column].values for column in data.columns[1:]])
            # 载入 note 数据
            for filePath in filePaths:
                if not filePath.endswith(FileEndName.JSON):
                    continue
                with open(filePath, "r", newline= "") as file:
                    self.note.loadData(json.load(file))
                break
        except Exception as e:
            logging.error(e)
            return False
        return True