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

    def loadData(self, timestamp: list, sensorTimestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.angularSpeedX = values[0]
        self.angularSpeedY = values[1]
        self.angularSpeedZ = values[2]
        self.angularSpeedXDrift = values[3]
        self.angularSpeedYDrift = values[4]
        self.angularSpeedZDrift = values[5]