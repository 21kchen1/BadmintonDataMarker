
"""
    数据读取服务
    负责根据路径读取需要的所有数据
    @author chen
"""

class DataRead:
    """
        设置字典，决定后续读取的数据类型
        @param modelDict 模型类型与实例字典
    """
    def __init__(self, modelDict: dict) -> None:
        self.modelDict = modelDict