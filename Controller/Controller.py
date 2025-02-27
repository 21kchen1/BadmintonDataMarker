from View.View import View

"""
    通用控制器
    @author chen
"""

class Controller:
    """
        @param view 视图
    """
    def __init__(self, view: View) -> None:
        self.view = view

    """
        设置槽函数
    """
    def setSlot(self) -> None:
        pass