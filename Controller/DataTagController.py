from Controller.Controller import Controller
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
        # 击球点与时间戳
        positionX, positionY, timestamp = self.dataTag.getPositionByIndex(self.nowPositionIndex)
        # 动作类型
        sportType = self.dataTag.getNoteSportType()
        # 设置
        self.view.ui.XLineEdit.setText(f"{positionX}")
        self.view.ui.YLineEdit.setText(f"{positionY}")
        self.view.ui.TimeSpinBox.setValue(timestamp)
        # 操作选项
        comboxIndex = self.view.ui.TypeComboBox.findText(sportType)
        if comboxIndex != -1:
            self.view.ui.TypeComboBox.setCurrentIndex(comboxIndex)
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
        击球点数据标签完成处理
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
        # 重置视图
        self.view.resetData()
        # 待机模式
        self.view.standbyMode()

    """
        有效
        获取标签，获取数据时间范围，生成数据单元，保存，下一个
    """
    def validData(self) -> None:
        # 获取标签
        label = self.getDataLabel()
        # 获取数据时间范围
        startTimestamp = int(self.view.ui.StartLineEdit.text())
        endTimestamp = int(self.view.ui.EndLineEdit.text())
        # 生成数据单元
        dataUnit = self.dataTag.createDataUnit(startTimestamp, endTimestamp, label)
        # 如果保存异常
        if not self.dataSave.saveDataUnit(dataUnit):
            self.view.errorShow(f"{String.ErrorInfo.STORAGE_FILE}\nPath: {self.dataSave.storePath}")
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
        开始标签
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

        # 开始标签
        self.view.ui.StartTagButton.clicked.connect(self.startTag)