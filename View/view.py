from os import name
from Resources import Integer
from Resources.String import Button
from View.MainUI import Ui_DataMarker
from View.VideoWidget import VideoWidget
from View.GraphWidget import GraphWidget
from PyQt5 import QtWidgets, QtCore
import sys
import matplotlib

# 设置图标字体
matplotlib.rcParams['font.family'] = 'Consolas'
matplotlib.rcParams['font.size'] = 20

"""
    视图，显示 GUI
    @auther chen
"""

class View:
    # 进度条最大值
    PROC_MAX = Integer.View.PROC_MAX
    # 选择按钮名称
    ACCE_RADIO = Button.ACCE_RADIO
    GYRO_RADIO = Button.GYRO_RADIO
    ROTATE_RADIO = Button.ROTATE_RADIO
    X_CHECK = Button.X_CHECK
    Y_CHECK = Button.Y_CHECK
    Z_CHECK = Button.Z_CHECK

    """
        初始化界面
        @param width 宽度
        @param height 高度
    """
    def __init__(self, width= 1500, height= 100) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWidget = QtWidgets.QWidget()
        # 主界面
        self.ui = Ui_DataMarker()
        self.width = width
        self.height = height
        # 运行模式 [false: 待机, true: 运行]
        self.mode = False
        self.uiInit()

    """
        设置关闭回调函数
        @param callback 回调函数
    """
    def setCloseCallback(self, callback) -> None:
        self.closeCallback = callback

    """
        关闭事件
    """
    def closeEvent(self, event) -> None:
        if self.closeCallback:
            self.closeCallback()
        self.app.quit()
        event.accept()

    """
        初始化 UI
    """
    def uiInit(self) -> None:
        self.ui.setupUi(self.mainWidget)
        self.mainWidget.resize(self.width, self.height)
        # 设置视频窗口
        self.VideoLayout = QtWidgets.QVBoxLayout(self.ui.VideoWidget)
        self.VideoWidget = VideoWidget(self.mainWidget)
        self.VideoWidget.setProgressMax(View.PROC_MAX)
        self.VideoLayout.addWidget(self.VideoWidget)
        # 设置图表窗口
        self.GraphLayout = QtWidgets.QVBoxLayout(self.ui.GraphWidget)
        self.GraphWidget = GraphWidget(self.mainWidget)
        self.GraphLayout.addWidget(self.GraphWidget)
        # 隐藏按钮 用于触发对应的服务
        self.ui.StartShowButton.setVisible(False)
        self.ui.StartTagButton.setVisible(False)
        # 计时器
        self.timer = QtCore.QTimer(self.mainWidget)
        # 关闭事件
        self.mainWidget.closeEvent = self.closeEvent
        # 设置模式
        self.standbyMode()

    """
        重置数据
        将视图数据初始化
    """
    def resetData(self) -> None:
        # 时间戳重置
        self.ui.TimeSpinBox.setValue(0)
        # 击球点坐标标签重置
        self.ui.XLineEdit.setText("")
        self.ui.YLineEdit.setText("")
        # 进度重置
        self.ui.SaveLineEdit.setText("")
        # 清除数据图表
        self.GraphWidget.clean()
        # 清除视频数据
        self.VideoWidget.clean()

    """
        待机模式
        文件设置与开始可用
    """
    def standbyMode(self) -> None:
        self.mode = False
        self.ui.TagFolderWidget.setEnabled(True)
        self.ui.TagSetWidget.setEnabled(False)
        self.ui.SetWidget.setEnabled(False)

    """
        载入模式
        全部禁用
    """
    def loadMode(self) -> None:
        self.mode = False
        self.ui.TagFolderWidget.setEnabled(False)
        self.ui.TagSetWidget.setEnabled(False)
        self.ui.SetWidget.setEnabled(False)

    """
        运行模式
        标签与图表设置可用
    """
    def runningMode(self) -> None:
        self.mode = True
        self.ui.TagFolderWidget.setEnabled(False)
        self.ui.TagSetWidget.setEnabled(True)
        self.ui.SetWidget.setEnabled(True)

    """
        开始展示
        触发开始展示按钮
    """
    def startShow(self) -> None:
        self.ui.StartShowButton.setEnabled(True)
        self.ui.StartShowButton.click()
        self.ui.StartShowButton.setEnabled(False)

    """
        开始标签
        触发开始标签按钮
    """
    def startTag(self) -> None:
        self.ui.StartTagButton.setEnabled(True)
        self.ui.StartTagButton.click()
        self.ui.StartTagButton.setEnabled(False)

    """
        文件夹路径设置
    """
    def selectFolder(self) -> str:
        return QtWidgets.QFileDialog.getExistingDirectory(self.mainWidget, "Select Folder")

    """
        设置计时器
        @param msec 间隔
    """
    def setTimer(self, msec: int) -> None:
        self.timer.start(msec)

    """
        停止计时器
    """
    def stopTimer(self) -> None:
        self.timer.stop()

    """
        错误窗口
        @param info 信息
    """
    def errorShow(self, info: str) -> None:
        QtWidgets.QMessageBox.critical(self.mainWidget, "Error", f" {info} ")

    """
        保存确定窗口
        @return bool 是否保存
    """
    def toSave(self) -> bool:
        return QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self.mainWidget, "Save DataSet File", "Whether to save a coordinate file?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

    """
        执行
    """
    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())