
"""
    存储 note.json 类
    @author chen
"""

class Note:
    """
        @param gender 性别
        @param exp 经验
        @param section 回合
        @param device 设备
    """
    def __init__(self, gender: str, exp: str, section: int, device: str, startTimestamp: int, endTimestamp: int) -> None:
        self.gender = gender
        self.exp = exp
        self.section = section
        self.device = device