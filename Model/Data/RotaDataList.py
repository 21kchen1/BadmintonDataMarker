
from Model.Data.TypeDataList import TypeDataList

"""
    RotationVector 数据列表·
    @author chen
"""

class RotaDataList(TypeDataList):
    TYPE = "ROTATION_VECTOR"

    def __init__(self) -> None:
        super().__init__(RotaDataList.TYPE)

    def loadData(self, timestamp: list, sensorTimestamp: list, *values: list) -> None:
        super().loadData(timestamp)
        self.sensorTimestamp = sensorTimestamp
        self.vectorX = values[0]
        self.vectorY = values[1]
        self.vectorZ = values[2]
        self.cosDelta = values[3]
        self.headingAccuracy = values[4]