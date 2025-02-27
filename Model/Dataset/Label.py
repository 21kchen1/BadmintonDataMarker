
"""
    数据存储单元标签
    @author chen
"""

class Label:
    """
        @param positionX 坐标 X
        @param positionY 坐标 Y
        @param actionType 动作类型
        @param actionEval 动作评价
    """
    def __init__(self, positionX: float, positionY: float, actionType: str, actionEval: str) -> None:
        self.positionX = positionX
        self.positionY = positionY
        self.actionType = actionType
        self.actionEval = actionEval