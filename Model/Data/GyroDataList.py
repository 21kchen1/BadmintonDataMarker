from Model.Data.TypeDataList import TypeDataList

"""
    Gyroscope 数据列表
    @author chen
"""

class GyroDataList(TypeDataList):
    TYPE = "GYROSCOPE"

    def __init__(self) -> None:
        super().__init__(GyroDataList.TYPE)

    def loadData(self, timestamp: list, sensorTimestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.angularSpeedX = values[0]
        self.angularSpeedY = values[1]
        self.angularSpeedZ = values[2]