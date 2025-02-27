# 原始字典
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 使用 list() 转换字典
keys_list = list(original_dict.items())

print(keys_list)  # 输出: ['a', 'b', 'c', 'd', 'e']

for key, item in original_dict.items():
    original_dict[key] = item * 10
print(original_dict)