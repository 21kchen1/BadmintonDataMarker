from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    AccelerometerU 数据类别
    @author chen
"""

class AcceUDataList(TypeDataList):
    # 类型标识
    TYPE = DataType.ACCE_U

    def __init__(self) -> None:
        super().__init__(AcceUDataList.TYPE)

    """
        @param timestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.Gx = valueLists[0]
        self.Gy = valueLists[1]
        self.Gz = valueLists[2]
        self.GxBias = valueLists[3]
        self.GyBias = valueLists[4]
        self.GzBias = valueLists[5]