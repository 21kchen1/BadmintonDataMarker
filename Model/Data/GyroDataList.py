from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    Gyroscope 数据列表
    @author chen
"""

class GyroDataList(TypeDataList):
    TYPE = DataType.GYRO

    def __init__(self) -> None:
        super().__init__(GyroDataList.TYPE)

    """
        @param timestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.sensorTimestamp = sensorTimestamp
        self.angularSpeedX = valueLists[0]
        self.angularSpeedY = valueLists[1]
        self.angularSpeedZ = valueLists[2]