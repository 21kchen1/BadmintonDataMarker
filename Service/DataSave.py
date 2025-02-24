
"""
    数据保存服务
    @author chen
"""

import os

from Resources.String import FileEndName


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
        with open(self.storePath, "w", newline= "", encoding= "utf-8") as _:
            pass
        return True