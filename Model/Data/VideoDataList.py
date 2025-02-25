from Model.Data.TypeDataList import TypeDataList
from Resources.String import DataType
import numpy as np
import cv2
import io

"""
    Video 数据列表
    @author chen
"""

class VideoDataList(TypeDataList):
    TYPE = DataType.VIDEO

    def __init__(self) -> None:
        super().__init__(VideoDataList.TYPE)

    """
        @param ttimestamp 系统时间戳
        @param width 视频宽度
        @param height 视频高度
        @param values 视频数据
    """
    def loadData(self, timestamp: list, width: list, height: list, *valueLists: list) -> None:
        super().loadData(timestamp, len(valueLists))
        self.width = width
        self.height = height
        self.values = valueLists[0]

    """
        将字符串数据转换为 opencv 图像
    """
    def procData(self) -> None:
        initDatas = self.values
        imageList = []
        for initData in initDatas:
            values = initData.strip('[]"')
            values = list(map(int, values.split(", ")))
            # 将字节列表转换为字节数据
            dataBytes = np.array(values, dtype=np.uint8).tobytes()
            # 使用 io.BytesIO 将字节数据转换为文件类对象
            imageData = io.BytesIO(dataBytes).getvalue()
            # 使用 cv2 读取图像数据
            imageList.append(cv2.imdecode(np.frombuffer(imageData, np.uint8), cv2.IMREAD_UNCHANGED))
        self.values = imageList