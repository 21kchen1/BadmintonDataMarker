import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSpinBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()

    def plot(self, data=None):
        ax = self.figure.add_subplot(111)
        ax.clear()

        if data is not None:
            for y in data:
                ax.plot(y[0], y[1])  # x 和 y 数据

        self.draw()


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 100
        self.top = 100
        self.title = 'Matplotlib + PyQt 动态图表'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton('更新图表', self)
        button.setToolTip('点击更新图表')
        button.clicked.connect(self.update_plot)
        button.move(500, 0)

        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(1, 10)  # 设置可变的线条数量
        self.spinBox.setValue(3)  # 默认值
        self.spinBox.move(500, 50)

        self.show()

    def update_plot(self):
        n = self.spinBox.value()  # 获取用户指定的线条数量
        x = np.linspace(0, 10, 100)  # 共同的 X 坐标
        data = [(x, np.sin(x + i * np.pi / 4)) for i in range(n)]  # 动态生成数据

        self.findChild(PlotCanvas).plot(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())