from Resources import Integer
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

    """
        @param dataShow 数据显示服务
        @param view 视图
    """
    def __init__(self, dataShow: DataShow, view: View) -> None:
        self.dataShow = dataShow
        self.view = view
        # 当前时间戳
        self.nowTimestamp = 0
        # 是否播放
        self.isPlaying = False

    """
        Time 设置
    """
    def timeSet(self) -> None:
        # 获取当前时间戳
        self.nowTimestamp = self.view.ui.TimeSpinBox.value()
        # 获取图像与进度
        image, percent = self.dataShow.getVideoQImage(self.nowTimestamp)
        self.view.VideoWidget.setImage(image)
        self.view.VideoWidget.setProgress(percent)

    """
        Step 设置
    """
    def stepSet(self) -> None:
        # 设置步长
        step = self.view.ui.StepSpinBox.value()
        self.view.ui.TimeSpinBox.setSingleStep(step)

    """
        Play 播放
    """
    def playData(self) -> None:
        # 如果正在播放
        if self.isPlaying:
            return
        self.view.setTimer(DataShowController.LOOP_INTER)
        self.isPlaying = True

    """
        Stop 暂停
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