from cProfile import label
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Resources.String import Graph

"""
    图表组件
    将传入的数据显示为图标
    @author chen
"""
class GraphWidget(QWidget):
    def __init__(self, parent= None) -> None:
        super(GraphWidget, self).__init__(parent)
        # 创建图表
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        # 将 canvas 添加到布局中
        self.vBoxLayout = QVBoxLayout(self.canvas)

    """
        清除所有图形
    """
    def clean(self) -> None:
        self.figure.clear()

    """
        绘制折线图
        @param title 标题
        @param timestamp 时间戳
        @param dataDict 数据字典
    """
    def plotLineChart(self, title: str, timestamp: list, dataDict: dict) -> None:
        # 清除
        self.clean()
        # 创建新图形
        ax = self.figure.add_subplot(111)
        # 设置标题
        ax.set_title(title)
        # 绘制数据
        for name, data in dataDict.items():
            ax.plot(timestamp, data, label(f"{name}"))
        ax.set_xlabel(Graph.XLabel)
        ax.set_ylabel(Graph.YLabel)
        # 刷新
        self.canvas.draw()