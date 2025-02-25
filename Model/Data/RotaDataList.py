
from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    RotationVector 数据列表·
    @author chen
"""

class RotaDataList(TypeDataList):
    TYPE = DataType.ROTA

    def __init__(self) -> None:
        super().__init__(RotaDataList.TYPE)

    """
        @param timestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.sensorTimestamp = sensorTimestamp
        self.vectorX = valueLists[0]
        self.vectorY = valueLists[1]
        self.vectorZ = valueLists[2]
        self.cosDelta = valueLists[3]
        self.headingAccuracy = valueLists[4]