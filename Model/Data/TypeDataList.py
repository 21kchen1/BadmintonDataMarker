from typing import Tuple, Union
from Resources import String
from Util.BSearch import bSearchL, bSearchR
import numpy

"""
    通用数据列表
    @author chen
"""

class TypeDataList:
    TIMESTAMP = String.DataType.TIMESTAMP
    LIST_LEN = String.DataType.LIST_LEN

    def __init__(self) -> None:
        self.timestamp = []
        self.listLen = 0

    """
        载入数据
        @param timestamp 时间戳
        @param valueNum 值数量
    """
    def loadData(self, timestamp: list, valueNum= 0) -> None:
        self.timestamp = timestamp
        self.listLen = len(self.timestamp)
        self.valueNum = valueNum

    """
        数据去重
        清除时间戳重叠的数据
    """
    def uniqueData(self) -> None:
        # 属性列表 只处理载入的列表数据
        # loadListName = {attrName:[] for attrName, attrValues in self.__dict__.items() if hasattr(attrValues, "__len__") and len(attrValues) == self.listLen}
        loadListName = [attrName for attrName, attrValues in self.__dict__.items() if hasattr(attrValues, "__len__") and len(attrValues) == self.listLen]
        # print(len(self.timestamp))
        # 写入索引，从第一个开始
        writerIndex = 1
        maxTimestamp = self.timestamp[0]
        for readIndex in range(1, len(self.timestamp)):
            # 如果现在值小于等之前的最大值
            if self.timestamp[readIndex] <= maxTimestamp:
                continue
            # 更大
            # 更新最大值
            maxTimestamp = self.timestamp[readIndex]
            for attrName in loadListName:
                self.__dict__[attrName][writerIndex] = self.__dict__[attrName][readIndex]
            writerIndex += 1
        # 清除无效部分
        for attrName in loadListName:
            self.__dict__[attrName] = self.__dict__[attrName][0 : writerIndex]
        # print(len(self.timestamp))
        # 更新数据长度
        self.listLen = len(self.timestamp)

    """
        清除数据
    """
    def cleanData(self) -> None:
        # 遍历属性并重置
        for key in self.__dict__.keys():
            setattr(self, key, None)
        self.timestamp = []
        self.listLen = 0

    """
        数据处理
    """
    def procData(self) -> None:
        pass

    """
        是否空数据
        @return bool 是否空
    """
    def emptyData(self) -> bool:
        return self.listLen <= 0

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
        @return int 大于等于 start 的时间戳下标
        @return int 小于等于 end 的时间戳下标
    """
    def getRangeIndex(self, start: int, end: int) -> Union[Tuple[int, int], Tuple[None, None]]:
        # 如果没有载入数据
        if self.listLen <= 0 or start > end:
            return None, None
        # 大于等于 start
        def __GES(mid: int) -> bool:
            return self.timestamp[mid] >= start
        # 小于等于 end
        def __LEE(mid: int) -> bool:
            return self.timestamp[mid] <= end

        return bSearchL(0, self.listLen - 1, __GES), bSearchR(0, self.listLen - 1, __LEE)

    """
        通过数字下标获取属性值
        下标：属性的定义顺序
        @param index 数字下标
        @return list 值
    """
    def getValueByIndex(self, index: int) -> Union[list, None]:
        if index >= self.valueNum:
            return None
        attrList = list(self.__dict__.keys())
        index = len(attrList) - self.valueNum + index
        return getattr(self, attrList[index])

    """
        通过数字下标获取时间戳
        下标：时间戳列表的下标
        @param index 数字下标
        @return int 时间戳
    """
    def getTimeStampByIndex(self, index: int) -> Union[int, None]:
        if index >= self.listLen:
            return None
        return self.timestamp[index]

    """
        获取属性字典
        @return dict 属性值字典
    """
    def getAttrDict(self) -> dict:
        attrList = list(self.__dict__.items())
        return dict(attrList[-self.valueNum : ])