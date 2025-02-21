from Model.Data.TypeDataList import TypeDataList

"""
    PICTURE 数据列表
    @author chen
"""

class PictureDataList(TypeDataList):
    TYPE = "PICTURE"

    def __init__(self) -> None:
        super().__init__(PictureDataList.TYPE)

    def loadData(self, timestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.xPosition = values[0]
        self.yPosition = values[1]