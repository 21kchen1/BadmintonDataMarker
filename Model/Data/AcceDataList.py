from Model.Data.TypeDataList import TypeDataList

"""
    Accelerometer 数据列表
    @author chen
"""

class AcceDataList(TypeDataList):
    # 类型标识
    TYPE = "ACCELEROMETER"

    def __init__(self) -> None:
        super().__init__(AcceDataList.TYPE)

    """
        @param unixTimestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.Gx = valueLists[0]
        self.Gy = valueLists[1]
        self.Gz = valueLists[2]
