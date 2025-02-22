import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.setWindowTitle("Matplotlib 折线图示例")
        self.resize(600, 400)

        # 创建 matplotlib 图形
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 创建布局并添加 canvas
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        # 绘制折线图
        self.plot_line_chart()

    def plot_line_chart(self):
        # 示例数据
        data = [10, 20, 30, 25, 40, 35, 50]

        # 清除之前的图形
        self.figure.clear()

        # 创建新的图形
        ax = self.figure.add_subplot(111)
        ax.plot(data, marker='o', linestyle='-')
        ax.set_title("折线图示例")
        ax.set_xlabel("X 轴")
        ax.set_ylabel("Y 轴")

        # 刷新 canvas
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MatplotlibWidget()
    window.show()
    sys.exit(app.exec_())