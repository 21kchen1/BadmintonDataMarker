from Model.Data.TypeDataList import TypeDataList

"""
    MagneticFieldU 数据列表
    @author chen
"""

class MagnUDataList(TypeDataList):
    TYPE = "MAGNETIC_FIELD_UNCALIBRATED"

    def __init__(self) -> None:
        super().__init__(MagnUDataList.TYPE)

    def loadData(self, timestamp: list, sensorTimestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.magneticFieldX = values[0]
        self.magneticFieldY = values[1]
        self.magneticFieldZ = values[2]
        self.magneticFieldXBias = values[3]
        self.magneticFieldYBias = values[4]
        self.magneticFieldZBias = values[5]