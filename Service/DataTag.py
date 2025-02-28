from Model.Data.TypeDataList import TypeDataList
from Model.Dataset.DataUnit import DataUnit
from Model.Dataset.Info import Info
from Model.Dataset.Label import Label
from Model.Note.Note import Note
from Resources.String import DataType

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
        获取击球点数量
        @return int 数量
    """
    def getPositionNum(self) -> int:
        positionData = self.modelDict.get(DataType.POSITION)
        if not positionData or positionData.emptyData():
            return None
        return positionData.listLen

    """
        根据下标获取击球点坐标与时间戳
        @param index 击球次数
        @return float 坐标 x
        @return float 坐标 y
        @return int 时间戳
    """
    def getPositionByIndex(self, index: int) -> tuple:
        positionData = self.modelDict.get(DataType.POSITION)
        # 无效或超过范围
        if not positionData or positionData.emptyData() or index >= positionData.listLen:
            return None, None, None
        # 获取击球点
        attrDict = list(positionData.getAttrDict().values())
        positionX = attrDict[0][index]
        positionY = attrDict[1][index]
        timestamp = positionData.getTimeStampByIndex(index)
        return positionX, positionY, timestamp

    """
        获取信息中动作类型
    """
    def getNoteSportType(self) -> str:
        return self.note.action

    """
        生成空数据存储单元
        @param startTimestamp 开始时间戳
        @param endTimestamp 结束时间戳
        @return DataUnit 数据存储单元
    """
    def createNoneDataUnit(self, startTimestamp: int, endTimestamp: int) -> DataUnit:
        # 生成信息
        info = Info(self.note, startTimestamp, endTimestamp)
        return DataUnit(info)

    """
        生成数据存储单元
        @param startTimestamp 开始时间戳
        @param endTimestamp 结束时间戳
        @param label 数据标签
        @param optimize 是否生成插值优化函数
        @return DataUnit 数据存储单元
    """
    def createDataUnit(self, startTimestamp: int, endTimestamp: int, label: Label, optimize= False) -> DataUnit:
        # 生成信息
        info = Info(self.note, startTimestamp, endTimestamp)
        # 截取的数据字典 {数据类型 : 截取数据}
        dataDict = {}
        # 获取需要保存的属性字典并截取数据
        for dataType in self.saveDataList:
            typeData = self.modelDict.get(dataType)
            # 如果是无效数据
            if not typeData or typeData.emptyData():
                continue
            # 获取属性字典
            attrDict = typeData.getAttrDict()
            # 获取区间下标
            sIndex, eIndex = typeData.getRangeIndex(startTimestamp, endTimestamp)
            # 存储属性时间戳
            attrDict[TypeDataList.TIMESTAMP] = typeData.timestamp
            # 遍历属性并截取其值
            for attrName, attrValueList in attrDict.items():
                attrDict[attrName] = list(attrValueList[sIndex : eIndex + 1])
            # 记录于数据字典
            dataDict[dataType] = attrDict
        # 无需优化
        if not optimize:
            return DataUnit(info, label, dataDict, None)
        # 对各个数据进行插值优化