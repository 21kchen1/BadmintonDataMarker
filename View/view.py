from View.MainUI import Ui_DataMarker
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

        # 关闭事件
        self.mainWidget.closeEvent = self.closeEvent

    """
        执行
    """
    def run(self) -> None:
        self.mainWidget.show()
        sys.exit(self.app.exec_())