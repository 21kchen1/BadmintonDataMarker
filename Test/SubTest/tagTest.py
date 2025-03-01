import json
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = "SimHei"
matplotlib.rcParams['font.size'] = 20

head = "G:\\Badminton\\TestData"
head = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData"
fileName = "Large.json"



dataUnitList = []
with open(os.path.join(head, fileName), "r", newline= "") as file:
    dataUnitList = json.load(file)

dataName = "data"
interDataName = "interData"
Timestamp = "timestamp"
dataTypeList = ["ACCELEROMETER", "GYROSCOPE", "GYROSCOPE_UNCALIBRATED", "MAGNETIC_FIELD", "MAGNETIC_FIELD_UNCALIBRATED", "ROTATION_VECTOR"]

for dataType in dataTypeList:
    for index in range(0, 2):
        AttrDict = dataUnitList[index][dataName][dataType]
        for attrName, attrValues in AttrDict.items():
            if attrName == Timestamp:
                continue
            plt.plot(AttrDict[Timestamp], attrValues, "o", label= attrName)

        AttrDict = dataUnitList[index][interDataName][dataType]

        for attrName, attrValues in AttrDict.items():
            if attrName == Timestamp:
                continue
            plt.plot(AttrDict[Timestamp], attrValues, "-", label= f"Inter {attrName}")
        plt.legend()
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
        plt.show()
