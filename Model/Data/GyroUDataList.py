from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    GyroscopeU 数据列表
    @author chen
"""

class GyroUDataList(TypeDataList):
    TYPE = DataType.GYRO_U

    def __init__(self) -> None:
        super().__init__(GyroUDataList.TYPE)

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
        self.angularSpeedXDrift = valueLists[3]
        self.angularSpeedYDrift = valueLists[4]
        self.angularSpeedZDrift = valueLists[5]