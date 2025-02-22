import sys
import time
sys.path.append("../")
from Service.DataLoad import DataLoad
import Main

testService = DataLoad(Main.MODEL_DICT)

bef = time.time()
testService.loadData("D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Small")
print(time.time() - bef)

for key, model in Main.MODEL_DICT.items():
    print(key)
    for name, value in model.__dict__.items():
        print(f"{name} : {value}")