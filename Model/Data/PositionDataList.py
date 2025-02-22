from Model.Data.TypeDataList import TypeDataList

"""
    POSITION 数据列表
    @author chen
"""

class PositionDataList(TypeDataList):
    TYPE = "POSITION"

    def __init__(self) -> None:
        super().__init__(PositionDataList.TYPE)

    def loadData(self, timestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.xPosition = values[0]
        self.yPosition = values[1]