from Util.BSearch import bSearchL, bSearchR

"""
    通用数据列表
    @author chen
"""

class TypeDataList:
    """
        @param t_type 数据类型
    """
    def __init__(self, t_type: str) -> None:
        self.type = t_type
        self.timestamp = []
        self.listLen = 0

    """
        载入数据
        @param timestamp 时间戳
    """
    def loadData(self, timestamp: list) -> None:
        self.timestamp = timestamp
        self.listLen = len(self.timestamp)

    """
        检测数据长度是否正确
        @param dataLists 若干个数据列表
        @return 这几个列表长度是否正确
    """
    def checkLen(self, *dataLists) -> bool:
        for dataList in dataLists:
            if len(dataList) == self.listLen:
                continue
            return False
        return True

    """
        通过时间戳范围获取下标
        @param start 起点时间戳
        @param end 终点时间戳
        @return 大于等于 start 的时间戳下标
        @return 小于等于 end 的时间戳下标
    """
    def getRangeIndex(self, start: int, end: int) -> int:
        # 大于等于 start
        def __GES(mid: int) -> bool:
            return self.timestamp[mid] >= start
        # 小于等于 end
        def __LEE(mid: int) -> bool:
            return self.timestamp[mid] <= end

        return bSearchL(0, self.listLen - 1, __GES), bSearchR(0, self.listLen - 1, __LEE)
