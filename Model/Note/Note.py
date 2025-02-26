
"""
    存储 note.json 类
    @author chen
"""

class Note:

    def __init__(self) -> None:
        self.gender = ""
        self.exp = ""
        self.time = ""
        self.other = ""

    """
        @param gender 性别
        @param exp 经验
        @param section 回合
        @param device 设备
    """
    def loadData(self, gender: str, exp: str, section: int, device: str) -> None:
        self.gender = gender
        self.exp = exp
        self.time = section
        self.other = device

    """
        使用字典动态赋值
    """
    def loadData(self, dataDict: dict) -> None:
        for key, value in dataDict.items():
            # 不是对应的属性
            if self.__dict__.get(key) == None:
                continue
            setattr(self, key, value)
