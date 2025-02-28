from copy import deepcopy
import numpy as np
import pandas as pd

head = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Large\\"

path = "ACCELEROMETER\\Man_Low_ForehandKill_LiZhiBang_1_2_ACCELEROMETER.csv"

file = pd.read_csv(head + path)

timestamps = file["unixTimestamp"].values

# 使用 np.unique 找到唯一值及其索引和计数
unique_timestamps, indices, counts = np.unique(timestamps, return_index=True, return_counts=True)

# 找到重复值（计数大于1）
duplicates = unique_timestamps[counts > 1]

# 找到重复值的所有下标
duplicate_indices = []
for dup in duplicates:
    indices = np.where(timestamps == dup)[0]  # 找到所有重复值的下标
    duplicate_indices.extend(indices)

# 去重并排序
duplicate_indices = sorted(set(duplicate_indices))

print("重复值的下标:", duplicate_indices)
print(len(duplicate_indices) / 2)

befNum = len(timestamps)
print(befNum - len(np.unique(timestamps)))

# 写入索引，从第一个开始
writerIndex = 1
maxTimestamp = timestamps[0]
for readIndex in range(1, len(timestamps)):
    # 如果和上一个相同
    if timestamps[readIndex] <= maxTimestamp:
        continue
    maxTimestamp = deepcopy(timestamps[readIndex])
    # 不同
    timestamps[writerIndex] = timestamps[readIndex]
    writerIndex += 1
# 清除无效部分

print(befNum - len(timestamps[0 : writerIndex]))