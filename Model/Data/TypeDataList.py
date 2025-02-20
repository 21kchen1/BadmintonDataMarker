
"""
    通用数据列表
    @author chen
"""

class TypeDataList:
    """
        @param t_type 数据类型
        @param unixTimestamp 时间戳
    """
    def __init__(self, t_type: str, unixTimestamp: list) -> None:
        self.type = t_type
        self.unixTimestamp = unixTimestamp
        self.listLen = len(self.unixTimestamp)

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
    """