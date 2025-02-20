from Model.Data.TypeDataList import TypeDataList

"""
    AccelerometerU 数据结构
    @author chen
"""

class AcceUDataList(TypeDataList):
    # 类型标识
    TYPE = "ACCELEROMETER_UNCALIBRATED"

    """
        @param unixTimestamp 系统时间戳
        @param sensorTimestamp 硬件时间戳
        @param valueLists 坐标轴列表
    """
    def __init__(self, unixTimestamp: list, sensorTimestamp: list, *valueLists: list) -> None:
        super().__init__(AcceUDataList.TYPE, unixTimestamp)
        self.sensorTimestamp = sensorTimestamp
        self.GxList = valueLists[0]
        self.GyList = valueLists[1]
        self.GzList = valueLists[2]
        self.GxBiasList = valueLists[3]
        self.GyBiasList = valueLists[4]
        self.GzBiasList = valueLists[5]