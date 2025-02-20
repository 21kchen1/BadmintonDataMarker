from Model.Data.TypeDataList import TypeDataList

"""
    Accelerometer 数据结构
    @author chen
"""

class AcceDataList(TypeDataList):
    # 类型标识
    TYPE = "ACCELEROMETER"

    """
        @param unixTimestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def __init__(self, unixTimestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().__init__(AcceDataList.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.GxList = valueLists[0]
        self.GyList = valueLists[1]
        self.GzList = valueLists[2]