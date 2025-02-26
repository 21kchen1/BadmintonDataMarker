
"""
    数据存储单元信息
    @author chen
"""

class Info:
    """
        @param gender 性别
        @param exp 经验
        @param section 回合
        @param device 设备
        @param startTimestamp 开始时间戳
        @param endTimestamp 结束时间戳
    """
    def __init__(self, gender: str, exp: str, section: int, device: str, startTimestamp: int, endTimestamp: int) -> None:
        self.gender = gender
        self.exp = exp
        self.section = section
        self.device = device
        self.startTimestamp = startTimestamp
        self.endTimestamp = endTimestamp