import sys
import time
sys.path.append("../")
from Model.Data.AcceDataList import AcceDataList
from Model.Data.TypeDataList import TypeDataList

testType = AcceDataList()
testType.loadData(*[[1], [2], [3], [4], [5]])
print(testType.__dict__)

testData = TypeDataList("TEST")
testData.loadData([i for i in range(0, 1145141000, 10)])
bef = time.time()
for _ in range(0, 10000):
    testData.getRangeIndex(10, 11451400)
print(time.time() - bef)