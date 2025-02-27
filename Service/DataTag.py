from Model.Note.Note import Note

"""
    数据标签服务
    负责返回指定数据类型数据
    @author chen
"""

class DataTag:

    """
        设置字典等数据,用于后续读取数据
        @param modelDict 模型类型与实例字典
        @param note 数据基本信息
        @param saveDataList 保存数据名称列表
    """
    def __init__(self, modelDict: dict, note: Note, saveDataList: list) -> None:
        self.modelDict = modelDict
        self.note = note
        self.saveDataList = saveDataList

    """
        根据下标获取击球点坐标与时间戳
        @param index 击球次数
        @return float 坐标 x
        @return float 坐标 y
        @return int 时间戳
    """
    def getPositionByIndex() -> None:
        pass