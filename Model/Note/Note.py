
"""
    存储 note.json 类
    @author chen
"""

class Note:

    def __init__(self) -> None:
        self.recordName = ""
        self.gender = ""
        self.exp = ""
        self.action = ""
        self.time = ""
        self.other = ""

    """
        @param recordName 记录名称
        @param gender 性别
        @param exp 经验
        @param action 动作类型
        @param section 回合
        @param device 设备
    """
    def loadData(self, recordName: str, gender: str, exp: str, action: str, section: int, device: str) -> None:
        self.recordName = recordName
        self.gender = gender
        self.exp = exp
        self.action = action
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
