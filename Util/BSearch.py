
"""
    二分查找
    @author chen
"""

"""
    左边界
    @param l 起点下标
    @param r 终点下标
    @param check(mid: int) 判断函数
    @return int 结果下标
"""
def bSearchL(l: int, r: int, check) -> int:
    while l < r:
        mid = l + r >> 1
        if check(mid): r = mid
        else: l = mid + 1
    return l

"""
    右边界
    @param l 起点下标
    @param r 终点下标
    @param check(mid: int) 判断函数
    @return int 结果下标
"""
def bSearchR(l: int, r: int, check) -> int:
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid): l = mid
        else: r = mid - 1
    return r