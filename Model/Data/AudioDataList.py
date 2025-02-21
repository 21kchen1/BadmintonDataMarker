from Model.Data.TypeDataList import TypeDataList

"""
    Audio 数据列表
    @author chen
"""

class AudioDataList(TypeDataList):
    TYPE = "AUDIO"

    def __init__(self) -> None:
        super().__init__(AudioDataList.TYPE)

    """
        @param timestamp 时间戳
    """
    def loadData(self, timestamp: list, samplingRate: list, *values: list) -> None:
        super().loadData(timestamp)
        self.samplingRate = samplingRate
        self.values = values[0]