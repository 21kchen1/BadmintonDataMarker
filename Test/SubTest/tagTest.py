import json
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Consolas'
matplotlib.rcParams['font.size'] = 30

head = "G:\\Badminton\\TestData"
# head = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData"
head = r"G:\Badminton\BADS_CLL_E_CLEAN_A"
# fileName = "TestJ.json"
fileName = "Man_Low_ForehandLob_LeiYang_1_1.json"


dataUnitList = []
with open(os.path.join(head, fileName), "r", newline= "") as file:
    dataUnitList = json.load(file)

dataName = "data"
interDataName = "interData"
Timestamp = "timestamp"
dataTypeList = ["AUDIO", "ACCELEROMETER", "GYROSCOPE", "MAGNETIC_FIELD", "ROTATION_VECTOR", "GYROSCOPE_UNCALIBRATED", "MAGNETIC_FIELD_UNCALIBRATED"]
# dataTypeList = ["GYROSCOPE"]

# 显示单组数据
# 第几个机器数据
index = 3
dataType = 0
# 未插值数据
AttrDict = dataUnitList[index][dataName][dataTypeList[0]]
attrName, attrValues = list(AttrDict.items())[dataType]
# 自定义时间戳
# timestamp = [time - AttrDict[Timestamp][0] for time in AttrDict[Timestamp]]
timestamp = AttrDict[Timestamp]
plt.plot(timestamp, attrValues, "o-", label= attrName)
# 插值数据
AttrDict = dataUnitList[index][interDataName][dataTypeList[0]]
attrName, attrValues = list(AttrDict.items())[dataType]
# timestamp = [time - AttrDict[Timestamp][0] for time in AttrDict[Timestamp]]
timestamp = AttrDict[Timestamp]
# plt.plot(timestamp, attrValues, "-", label= f"Cubic Interpolation {attrName}")
# plt.legend(loc='lower left')
plt.title("Backswing and Hit")
plt.legend(loc='upper left')
plt.xlabel("Timestamp (ms)")
plt.ylabel("Gyroscope y (rad/s)")
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

# 显示多组数据
for dataType in dataTypeList:
    for index in range(0, 3):
        AttrDict = dataUnitList[index][dataName][dataType]
        for attrName, attrValues in AttrDict.items():
            if attrName == Timestamp:
                continue
            timestamp = AttrDict[Timestamp]
            plt.plot(timestamp, attrValues, "o-", label= attrName)

        AttrDict = dataUnitList[index][interDataName][dataType]

        for attrName, attrValues in AttrDict.items():
            if attrName == Timestamp:
                continue
            timestamp = AttrDict[Timestamp]
            plt.plot(timestamp, attrValues, "-", label= f"Inter {attrName}")
        plt.title("Backswing and Hit")
        plt.legend(loc='upper right')
        plt.xlabel("Timestamp (ms)")
        plt.ylabel("Gyroscope (rad/s)")
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()
        plt.show()
