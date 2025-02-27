import sys
import time
sys.path.append("../../")
from Model.Data.AcceDataList import AcceDataList
from Model.Data.TypeDataList import TypeDataList

testType = AcceDataList()
testType.loadData(*[[1], [2], [3], [4], [5]])
print(testType.__dict__)

testData = TypeDataList("TEST")
testData.loadData([i for i in range(0, 114514, 2)])
print(testData.getRangeIndex(10, 11451))
bef = time.time()
for _ in range(0, 10000):
    testData.getRangeIndex(10, 11451)
print(time.time() - bef)

testData.loadData([1, 1, 1, 1, 1])
print(testData.getRangeIndex(1, 1))