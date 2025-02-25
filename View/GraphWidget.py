import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication
import matplotlib
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
    def __init__(self, parent= None) -> None:
        super(GraphWidget, self).__init__(parent)
        # 创建图表
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        # 将 canvas 添加到布局中
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.canvas)

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
        @param flagTime 提示中心
        @param flagRange 提示范围
    """
    def setPlotLineChart(self, title: str, timestamp: list, dataDict: dict, flagTime: int, flagRange= 0) -> None:
        # 清除
        self.clean()
        # 创建新图形
        ax = self.figure.add_subplot(111)
        # 设置标题
        ax.set_title(title)
        # 绘制数据
        for name, data in dataDict.items():
            ax.plot(timestamp, data, label= f"{name}")
        # 设置提示
        ax.axvline(x= flagTime, color= "g", linestyle='--', linewidth=1)
        if flagRange > 0:
            ax.axvline(x= flagTime + flagRange / 2, color= "r", linestyle='--', linewidth=1)
            ax.axvline(x= flagTime - flagRange / 2, color= "r", linestyle='--', linewidth=1)
        # 设置标签与字体
        ax.set_xlabel(Graph.X_LABEL)
        ax.set_ylabel(Graph.Y_LABEL)
        ax.tick_params(axis='both', labelsize= matplotlib.rcParams['font.size'] / 3 * 2)
        ax.legend()
        # 刷新
        self.canvas.draw()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = GraphWidget()
    window.setPlotLineChart("11", [1, 2], {})

    window.show()
    sys.exit(app.exec_())