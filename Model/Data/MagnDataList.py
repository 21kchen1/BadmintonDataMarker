from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    MagneticField 数据列表
    @author chen
"""

class MagnDataList(TypeDataList):
    TYPE = DataType.MAGN

    def __init__(self) -> None:
        super().__init__(MagnDataList.TYPE)

    def loadData(self, timestamp: list, sensorTimestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.magneticFieldX = values[0]
        self.magneticFieldY = values[1]
        self.magneticFieldZ = values[2]