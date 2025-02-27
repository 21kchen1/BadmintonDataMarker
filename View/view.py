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

        self.uiInit()

    """
        关闭事件
    """
    def closeEvent(self, event) -> None:
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
        # 隐藏按钮 用于表示
        self.ui.LoadSucceedButton.setVisible(False)

        # 计时器
        self.timer = QtCore.QTimer(self.mainWidget)

        # 关闭事件
        self.mainWidget.closeEvent = self.closeEvent
        # 设置模式
        self.standbyMode()

    """
        待机模式
        文件设置与开始可用
    """
    def standbyMode(self) -> None:
        self.ui.TagFolderWidget.setEnabled(True)
        self.ui.TagSetWidget.setEnabled(False)
        self.ui.SetWidget.setEnabled(False)

    """
        载入模式
        全部禁用
    """
    def loadMode(self) -> None:
        self.ui.TagFolderWidget.setEnabled(False)
        self.ui.TagSetWidget.setEnabled(False)
        self.ui.SetWidget.setEnabled(False)

    """
        运行模式
        标签与图表设置可用
    """
    def runningMode(self) -> None:
        self.ui.TagFolderWidget.setEnabled(False)
        self.ui.TagSetWidget.setEnabled(True)
        self.ui.SetWidget.setEnabled(True)

    """
        载入成功
        触发载入成功按钮
    """
    def loadSucceed(self) -> None:
        self.ui.LoadSucceedButton.setEnabled(True)
        self.ui.LoadSucceedButton.click()
        self.ui.LoadSucceedButton.setEnabled(False)

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
        执行
    """
    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())