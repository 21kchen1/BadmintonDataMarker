from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    POSITION 数据列表
    @author chen
"""

class PositionDataList(TypeDataList):
    TYPE = DataType.POSITION

    """
        @param timestamp 系统时间戳
        @param valueLists 坐标轴列表
    """
    def loadData(self, timestamp: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.xPosition = valueLists[0]
        self.yPosition = valueLists[1]