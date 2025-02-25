import sys
import time
sys.path.append("../")
from Resources.String import DataType
from Service.DataLoad import DataLoad
import Main

testService = DataLoad(Main.MODEL_DICT)

S = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Small"
L = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Large"

bef = time.time()
testService.loadData(S)
print(time.time() - bef)

for key, model in Main.MODEL_DICT.items():
    print(key)
    for name, value in model.__dict__.items():
        print(f"{name} : {value}")

print()
print(Main.MODEL_DICT[DataType.ACCE].getValuesByIndex(0))