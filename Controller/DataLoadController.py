from Controller.Controller import Controller
from Resources.String import ErrorInfo
from Service.DataLoad import DataLoad
from Service.DataSave import DataSave
from View.View import View

"""
    数据载入控制器
    负责 View 的 DataLoad 部分
    @author chen
"""

class DataLoadController(Controller):
    """
        @param dataLoad 数据载入服务
        @param dataSave 数据保存服务
        @param view 视图
    """
    def __init__(self, dataLoad: DataLoad, dataSave: DataSave, view: View) -> None:
        super().__init__(view)
        self.dataLoad = dataLoad
        self.dataSave = dataSave
        self.rootPath = None

    """
        槽函数
    """

    """
        选择文件夹
        测试文件路径并显示于视图
    """
    def selectFolder(self) -> None:
        # 选择路径
        rootPath = self.view.selectFolder()
        if not rootPath:
            return
        # 检测路径
        if not self.dataSave.checkPath(rootPath):
            self.view.errorShow(ErrorInfo.SELECT_FOLDER)
            return
        self.rootPath = rootPath
        self.view.ui.TagFolderLineEdit.setText(f" {self.rootPath} ")

    """
        开始处理
        载入数据
    """
    def startProcess(self) -> None:
        if not self.rootPath:
            self.view.errorShow(ErrorInfo.DATALOAD_PATH)
            return
        # 数据载入
        self.view.loadMode()
        if not self.dataLoad.loadData(self.rootPath):
            self.view.errorShow(ErrorInfo.DATALOAD)
            self.view.standbyMode()
            return
        # 创建数据文件
        self.dataSave.createSave(self.rootPath)
        self.view.runningMode()
        # 开始标签
        self.view.startTag()
        # 开始显示
        self.view.startShow()
        self.rootPath = None

    """
        设置槽函数
    """
    def setSlot(self) -> None:
        self.view.ui.SelectFolderButton.clicked.connect(self.selectFolder)
        self.view.ui.TagStartButton.clicked.connect(self.startProcess)