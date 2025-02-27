from Controller.Controller import Controller
from Service.DataSave import DataSave
from Service.DataTag import DataTag
from View.View import View

"""
    数据标签控制器
    负责 View 的 Tag 部分
    @author chen
"""

class DataTagController(Controller):

    """
        @param dataTag 数据标签服务
        @param dataSave 数据保存服务
        @param view 视图
    """
    def __init__(self, dataTag: DataTag, dataSave: DataSave, view: View) -> None:
        super().__init__(view)
        self.dataTag = dataTag
        self.dataSave = dataSave

    

    """
        设置槽函数
    """
    def setSlot(self) -> None:
        pass