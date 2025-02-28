from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    MagneticFieldU 数据列表
    @author chen
"""

class MagnUDataList(TypeDataList):
    TYPE = DataType.MAGN_U

    """
        @param timestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.sensorTimestamp = sensorTimestamp
        self.magneticFieldX = valueLists[0]
        self.magneticFieldY = valueLists[1]
        self.magneticFieldZ = valueLists[2]
        self.magneticFieldXBias = valueLists[3]
        self.magneticFieldYBias = valueLists[4]
        self.magneticFieldZBias = valueLists[5]