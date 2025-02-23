import sys
sys.path.append("../")

from Service.DataSave import DataSave
from Main import MODEL_DICT

test = DataSave(MODEL_DICT)

print(test.checkPath("../Test/TestData/Large"))
test.createSave("../Test/TestData/Small")