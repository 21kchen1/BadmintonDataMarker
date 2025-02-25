import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
import matplotlib
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
sys.path.append("../")
from Resources.String import Graph

"""
    图表组件
    将传入的数据显示为图标
    @author chen
"""
class GraphWidget(QWidget):
    COLORS = ['blue', 'orangered', 'gold', 'brown', 'purple', 'pink', 'gray', 'olive', 'cyan', 'yellow', 'green', 'red']

    def __init__(self, parent= None) -> None:
        super(GraphWidget, self).__init__(parent)
        # 创建图表
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        # 将 canvas 添加到布局中
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.canvas)

        # 初始化子图
        self.ax = self.figure.add_subplot(111)
        # 存储线条的引用
        self.lines = []
        # 设置标签与字体
        self.ax.set_xlabel(Graph.X_LABEL)
        self.ax.set_ylabel(Graph.Y_LABEL)
        self.ax.tick_params(axis='both', labelsize= matplotlib.rcParams['font.size'] / 3 * 2)

    """
        清除所有图形
    """
    def clean(self) -> None:
        # 清除线条
        for line in self.lines:
            line.remove()
        self.lines = []
        # 清除标题
        self.ax.set_title("")

    """
        绘制折线图
        @param title 标题
        @param timestamp 时间戳
        @param dataDict 数据字典
        @param flagTime 提示中心
        @param flagRange 提示范围
        @param update 更新坐标轴
    """
    def setPlotLineChart(self, title: str, timestamp: list, dataDict: dict, flagTime: int, flagRange: int, update= True) -> None:
        # 清除
        self.clean()

        # 设置标题
        self.ax.set_title(title)
        # 绘制数据
        for i, (name, data) in enumerate(dataDict.items()):
            # 设置颜色
            color = GraphWidget.COLORS[i % len(GraphWidget.COLORS)]
            line, = self.ax.plot(timestamp, data, label= f"{name}", color= color)
            self.lines.append(line)
        # 设置提示
        self.lines.append(self.ax.axvline(x= flagTime, color= "g", linestyle='--', linewidth=1))
        if flagRange > 0:
            self.lines.append(self.ax.axvline(x= flagTime + flagRange / 2, color= "r", linestyle='--', linewidth=1))
            self.lines.append(self.ax.axvline(x= flagTime - flagRange / 2, color= "r", linestyle='--', linewidth=1))

        # 更新轴范围
        self.ax.set_xlim(timestamp[0], timestamp[-1])
        if update:
            y_min = np.min([np.min(data) for data in dataDict.values()])
            y_max = np.max([np.max(data) for data in dataDict.values()])
            y_bias = (y_max - y_min) * 0.3
            self.ax.set_ylim(y_min - y_bias, y_max + y_bias)
        self.ax.legend(loc='upper left')
        # 刷新
        self.canvas.draw()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = GraphWidget()
    window.setPlotLineChart("11", [1, 2], {})

    window.show()
    sys.exit(app.exec_())