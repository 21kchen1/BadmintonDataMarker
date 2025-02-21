import sys
import time
sys.path.append("../")
from Model.Data.TypeDataList import TypeDataList

testData = TypeDataList("TEST", [i for i in range(0, 1145141000, 10)])

bef = time.time()
for _ in range(0, 10000):
    testData.getRangeIndex(10, 11451400)
print(time.time() - bef)