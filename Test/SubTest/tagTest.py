import json
import os
import numpy as np
from scipy.interpolate import interp1d
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

index = 2

x = dataUnitList[index]["data"]["ACCELEROMETER"]["timestamp"]
y = dataUnitList[index]["data"]["ACCELEROMETER"]["Gx"]
y1 = dataUnitList[index]["data"]["ACCELEROMETER"]["Gy"]
y2 = dataUnitList[index]["data"]["ACCELEROMETER"]["Gz"]

plt.plot(x, y, 'o', label='Gx')
plt.plot(x, y1, 'o', label='Gy')
plt.plot(x, y2, 'o', label='Gz')

newx = dataUnitList[index]["interData"]["ACCELEROMETER"]["timestamp"]
newy = dataUnitList[index]["interData"]["ACCELEROMETER"]["Gx"]
newy1 = dataUnitList[index]["interData"]["ACCELEROMETER"]["Gy"]
newy2 = dataUnitList[index]["interData"]["ACCELEROMETER"]["Gz"]

plt.plot(newx, newy, '-', label='插值后 Gx')
plt.plot(newx, newy1, '-', label='插值后 Gy')
plt.plot(newx, newy2, '-', label='插值后 Gz')
plt.legend()
plt.show()