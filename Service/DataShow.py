from PyQt5.QtGui import QImage
import numpy as np
import cv2
import io

from Resources.String import DataType

"""
    数据展示服务
    负责视频播放与数据图表展示
    @author chen
"""

class DataShow:
    """
        设置字典，决定后续读取的数据类型
        @param modelDict 模型类型与实例字典
    """
    def __init__(self, modelDict: dict) -> None:
        self.modelDict = modelDict

    """
        根据下标获取类型数据百分比
    """
    def getTypePercent(self, typeString: str, index: int) -> float:
        return float(index + 1) / self.modelDict[typeString].listLen

    """
        根据时间戳获取最接近的图像
        @param timestamp 时间戳
        @return QImage 图像
        @return float 进度百分比
    """
    def getVideoQImage(self, timestamp: int) -> QImage:
        if not self.modelDict.get(DataType.VIDEO):
            return None, None
        # 获取图像数据
        index, _ = self.modelDict[DataType.VIDEO].getRangeIndex(timestamp, timestamp)
        values = self.modelDict[DataType.VIDEO].values[index]
        # 处理数据
        values = list(map(int, values.strip('[]"').split(", ")))
        dataBytes = np.array(values, dtype=np.uint8).tobytes()
        # 使用 io.BytesIO 将字节数据转换为文件类对象
        imageData = io.BytesIO(dataBytes).getvalue()
        # 使用 cv2 读取图像数据
        image = cv2.imdecode(np.frombuffer(imageData, np.uint8), cv2.IMREAD_UNCHANGED)
        # 将 OpenCV 图像转换为 QImage
        height, width, _ = image.shape
        bytes_per_line = 3 * width
        return QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped(), \
                self.getTypePercent(DataType.VIDEO, index)

    """
        根据时间戳获取范围数据
        @param type 数据类型
        @param attr 属性下标
        @param start 起点
        @param end 终点
        @return list 时间戳
        @return list 数值
    """