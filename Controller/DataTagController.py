from Controller.Controller import Controller
from Model.Dataset.DataUnit import DataUnit
from Model.Dataset.Label import Label
from Resources import Integer, String
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
        # 现在击球点下标
        self.nowPositionIndex = 0
        # 现在时间戳
        self.nowTimestamp = 0

    """
        槽函数
    """

    """
        更新 section
    """
    def updateSection(self) -> None:
        self.nowTimestamp = self.view.ui.TimeSpinBox.value()
        self.view.ui.StartLineEdit.setText(f"{max(int(self.nowTimestamp - Integer.Controller.HALF_DATA_LEN), 0)}")
        self.view.ui.EndLineEdit.setText(f"{int(self.nowTimestamp + Integer.Controller.HALF_DATA_LEN)}")

    """
        根据当前击球点下标更新 tag 与 时间戳
    """
    def updateTagAndTimestamp(self) -> None:
        # 动作类型
        sportType = self.dataTag.getNoteSportType()
        # 操作选项
        comboxIndex = self.view.ui.TypeComboBox.findText(sportType)
        if comboxIndex != -1:
            self.view.ui.TypeComboBox.setCurrentIndex(comboxIndex)
        # 如果击球点数据异常
        if self.dataTag.getPositionNum() == None:
            return
        
        # 击球点与时间戳
        positionX, positionY, timestamp = self.dataTag.getPositionByIndex(self.nowPositionIndex)
        # 设置
        self.view.ui.XLineEdit.setText(f"{positionX}")
        self.view.ui.YLineEdit.setText(f"{positionY}")
        self.view.ui.TimeSpinBox.setValue(timestamp)
        # 进度更新
        self.view.ui.SaveLineEdit.setText(f"{self.nowPositionIndex + 1} / {self.dataTag.getPositionNum()}")

    """
        获取当前标签
        @return Label 数据标签
    """
    def getDataLabel(self) -> Label:
        positionX = float(self.view.ui.XLineEdit.text())
        positionY = float(self.view.ui.YLineEdit.text())
        actionType = self.view.ui.TypeComboBox.currentText()
        actionEval = self.view.ui.EvalComboBox.currentText()
        return Label(positionX, positionY, actionType, actionEval)

    """
        数据标签完成处理
        判断是否保存，重载视图
    """
    def finishTagProcess(self) -> None:
        # 视图状态显示未运行
        if not self.view.mode:
            return

        # 如果不保存，删除
        if not self.view.toSave():
            self.dataSave.deleteSave()

        # 重置进度
        self.nowPositionIndex = 0
        # 待机模式
        self.view.standbyMode()
        # 重置视图
        self.view.resetData()

    """
        数据标签保存处理
        保存后判断是否完成
        完成：结束进程
        未完成：下一个
        @param dataUnit 数据标签
    """
    def saveTagProcess(self, dataUnit: DataUnit) -> None:
        # 如果保存异常
        if not self.dataSave.saveDataUnit(dataUnit):
            self.view.errorShow(f"{String.ErrorInfo.STORAGE_FILE}\nPath: {self.dataSave.storePath}")
            return
        # 如果击球点数据异常，不设置自动更新
        if self.dataTag.getPositionNum() == None:
            return
        # 如果完成
        if self.nowPositionIndex + 1 >= self.dataTag.getPositionNum():
            self.finishTagProcess()
            return
        # 未完成，下一个
        self.nowPositionIndex += 1
        # 显示
        self.updateTagAndTimestamp()

    """
        有效
        获取标签，获取数据时间范围，生成数据单元，保存进程
    """
    def validData(self) -> None:
        # 获取标签
        label = self.getDataLabel()
        # 获取数据时间范围
        startTimestamp = int(self.view.ui.StartLineEdit.text())
        endTimestamp = int(self.view.ui.EndLineEdit.text())
        # 生成数据单元
        dataUnit = self.dataTag.createDataUnit(startTimestamp, endTimestamp, label)
        # 保存进程
        self.saveTagProcess(dataUnit)


    """
        无效
        获取数据时间范围，生成无效数据单元，保存进程
    """
    def invalidData(self) -> None:
        # 获取数据时间范围
        startTimestamp = int(self.view.ui.StartLineEdit.text())
        endTimestamp = int(self.view.ui.EndLineEdit.text())
        # 生成无效数据单元
        noneDataUnit = self.dataTag.createNoneDataUnit(startTimestamp, endTimestamp)
        # 保存进程
        self.saveTagProcess(noneDataUnit)


    """
        取消
        删除最后一个保存的数据，返回到上一个坐标点
    """
    def cancelData(self) -> None:
        pass

    """
        开始进行标签
    """
    def startTag(self) -> None:
        self.updateTagAndTimestamp()

    """
        设置槽函数
    """
    def setSlot(self) -> None:
        # 设置视图关闭函数
        self.view.setCloseCallback(self.finishTagProcess)
        # 更新 section
        self.view.ui.TimeSpinBox.valueChanged.connect(self.updateSection)
        # 有效
        self.view.ui.ValidButton.clicked.connect(self.validData)
        # 无效
        self.view.ui.InvalidButton.clicked.connect(self.invalidData)
        # 开始标签
        self.view.ui.StartTagButton.clicked.connect(self.startTag)