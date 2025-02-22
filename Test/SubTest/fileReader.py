import os

def get_all_file_paths(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

# 示例用法
directory = "..\Test"  # 替换为你的文件夹路径
file_paths = get_all_file_paths(directory)
for path in file_paths:
    print(path)