from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType

"""
    Audio 数据列表
    @author chen
"""

class AudioDataList(TypeDataList):
    TYPE = DataType.AUDIO

    def __init__(self) -> None:
        super().__init__(AudioDataList.TYPE)

    """
        @param timestamp 时间戳
        @param samplingRate 采样率
        @param valueLists 数值列表
    """
    def loadData(self, timestamp: list, samplingRate: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.samplingRate = samplingRate
        self.values = valueLists[0]