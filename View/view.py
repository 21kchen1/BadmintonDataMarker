from View.MainUI import Ui_DataMarker
from View.VideoWidget import VideoWidget
from PyQt5 import QtWidgets, QtCore
import sys

"""
    视图，显示 GUI
    @auther chen
"""

class View:
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
        self.mainWidget.setMinimumSize(QtCore.QSize(self.width, self.height))

        self.vBoxLayout = QtWidgets.QVBoxLayout(self.ui.VideoWidget)
        self.VideoWidget = VideoWidget(self.mainWidget)
        self.vBoxLayout.addWidget(self.VideoWidget)

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
        文件夹路径设置
    """
    def selectFolder(self) -> str:
        return QtWidgets.QFileDialog.getExistingDirectory(self.mainWidget, "Select Folder")

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