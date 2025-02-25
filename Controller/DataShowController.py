from Resources import Integer
from Resources.String import DataType
from Service.DataShow import DataShow
from View.View import View

"""
    数据显示控制器
    负责 View 的 DataShow 部分
    @author chen
"""

class DataShowController:
    # 循环定时器间隔 100 ms
    LOOP_INTER = Integer.Controller.LOOP_INTER

    # RadioButton 与 DataType 的映射
    RADIO_TYPE_DICT = {
        View.ACCE_RADIO: DataType.ACCE,
        View.GYRO_RADIO: DataType.GYRO,
        View.ROTATE_RADIO: DataType.ROTA,
    }

    # CheckButton 与 数据属性的映射
    CHECK_ATTR_DICT = {
        View.X_CHECK: (0, "X"),
        View.Y_CHECK: (1, "Y"),
        View.Z_CHECK: (2, "Z"),
    }

    """
        @param dataShow 数据显示服务
        @param view 视图
    """
    def __init__(self, dataShow: DataShow, view: View) -> None:
        self.dataShow = dataShow
        self.view = view
        # 是否播放
        self.isPlaying = False
        # 当前时间戳
        self.nowTimestamp = 0
        # 当前进度
        self.nowProcess = 0
        # 当前数据类型
        self.nowDataType = None
        # 当前属性列表
        self.nowAttrList = []
        # 当前显示时间访问
        self.nowTimeRange = 0

    """
        功能函数
    """

    """
        获取 DataType 设置
        @return str 选择的数据类型
    """
    def getDataTypeSet(self) -> str:
        for name, dataType in DataShowController.RADIO_TYPE_DICT.items():
            # 尝试获取按钮
            button = getattr(self.view.ui, name)
            # 不存在或未选中
            if not button or not button.isChecked():
                continue
            return dataType

    """
        获取 Axis 设置
        return list 选择的数据属性
    """
    def getAxisSet(self) -> list:
        axisList = []
        for name, axis in DataShowController.CHECK_ATTR_DICT.items():
            # 尝试获取按钮
            button = getattr(self.view.ui, name)
            # 不存在或未选中
            if not button or not button.isChecked():
                continue
            axisList.append(axis)
        return axisList

    """
        槽函数
    """

    """
        使用当前设置显示图表
    """
    def showGraph(self) -> None:
        # 设置异常
        if not self.nowDataType or not self.nowTimeRange:
            return

        # 范围时间戳
        sIndex = self.nowTimestamp - self.nowTimeRange / 2
        eIndex = self.nowTimestamp + self.nowTimeRange / 2
        # 获取时间戳
        timestamp = self.dataShow.getTypeDataTimestamp(self.nowDataType, sIndex, eIndex)

        # 标签与数据字典
        dataDict = {}
        # 遍历设置并获取数据
        for attr in self.nowAttrList:
            label = attr[1]
            data = self.dataShow.getTypeDataValue(self.nowDataType, attr[0], sIndex, eIndex)
            dataDict[label] = data

        # 提示范围
        flagRange = 0
        if self.nowTimeRange >= Integer.Controller.DATA_LEN:
            flagRange = Integer.Controller.DATA_LEN
        # 设置并显示图表
        self.view.GraphWidget.setPlotLineChart(self.nowDataType, timestamp, dataDict, self.nowTimestamp, flagRange)

    """
        Apply Graph 设置
        读取 DataType，Axis 与 数据显示范围
        更新 Graph
    """
    def applyGraphSet(self) -> None:
        # 获取所有属性
        self.nowDataType = self.getDataTypeSet()
        self.nowAttrList = self.getAxisSet()
        self.nowTimeRange = self.view.ui.RangeSpinBox.value()
        # 更新图表
        self.showGraph()

    """
        Time 设置
        显示视频与图表
    """
    def timeSet(self) -> None:
        # 获取当前时间戳
        self.nowTimestamp = self.view.ui.TimeSpinBox.value()
        # 获取图像与进度
        image, self.nowProcess = self.dataShow.getVideoQImage(self.nowTimestamp)
        self.view.VideoWidget.setImage(image)
        self.view.VideoWidget.setProgress(self.nowProcess)
        # 更新图表
        self.showGraph()

    """
        Step 设置
        设置视频速度
    """
    def stepSet(self) -> None:
        # 设置步长
        step = self.view.ui.StepSpinBox.value()
        self.view.ui.TimeSpinBox.setSingleStep(step)

    """
        Play 播放
        播放视频，设置计时器，定时执行 playLoop 函数
    """
    def playData(self) -> None:
        # 如果正在播放
        if self.isPlaying:
            return
        self.view.setTimer(DataShowController.LOOP_INTER)
        self.isPlaying = True

    """
        Stop 暂停
        暂停视频
    """
    def stopData(self) -> None:
        # 如果没有播放
        if not self.isPlaying:
            return
        self.view.stopTimer()
        self.isPlaying = False

    """
        与定时器关联的定时执行函数
        控制数据的持续播放
    """
    def playLoop(self) -> None:
        # 如果播放完成
        if self.nowProcess >= 1:
            self.stopData()
            return
        # 步长
        step = self.view.ui.StepSpinBox.value()
        # 改变时间戳
        self.view.ui.TimeSpinBox.setValue(self.nowTimestamp + step)

    """
        设置槽函数
    """
    def setSlot(self) -> None:
        self.view.ui.TimeSpinBox.valueChanged.connect(self.timeSet)
        self.view.ui.StepSpinBox.valueChanged.connect(self.stepSet)
        # 播放与停止
        self.view.ui.PlayButton.clicked.connect(self.playData)
        self.view.ui.StopButton.clicked.connect(self.stopData)
        self.view.timer.timeout.connect(self.playLoop)
        # 图表
        self.view.ui.ApplyButton.clicked.connect(self.applyGraphSet)