from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    Video 数据列表
    @author chen
"""

class VideoDataList(TypeDataList):
    TYPE = DataType.VIDEO

    def __init__(self) -> None:
        super().__init__(VideoDataList.TYPE)

    """
        @param unixTimestamp 系统时间戳
        @param width 视频宽度
        @param height 视频高度
        @param values 视频数据
    """
    def loadData(self, timestamp: list, width: list, height: list, *values: list) -> None:
        super().loadData(timestamp)
        self.width = width
        self.height = height
        self.values = values[0]
