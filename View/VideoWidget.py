import sys
from PyQt5 import QtWidgets, QtGui
import cv2

"""
    图像组件
    显示传入图像
"""
class ImageWidget(QtWidgets.QWidget):
    def __init__(self, parent= None) -> None:
        super(ImageWidget, self).__init__(parent)
        self.image = None

    """
        设置图像
        @param image QImage 格式的图像
    """
    def setImage(self, image: QtGui.QImage) -> None:
        self.image = image
        self.update()

    """
        重写子绘制函数
    """
    def paintEvent(self, event) -> None:
        qp = QtGui.QPainter()
        # 开始绘制
        qp.begin(self)

        if isinstance(self.image, QtGui.QImage):
            qp.drawPixmap(self.rect(), QtGui.QPixmap.fromImage(self.image))

        qp.end()


"""
    视频组件
    显示传入的图像并显示视频进度
    @author: chen
"""

class VideoWidget(QtWidgets.QWidget):
    """
        初始化
        @param parent 父组件
    """
    def __init__(self, parent= None) -> None:
        super(VideoWidget, self).__init__(parent)
        self.uiInit()

    """
        上下结构
        上图片
        下进度
    """
    def uiInit(self) -> None:
        self.MainLayout = QtWidgets.QVBoxLayout(self)
        self.ImageWidget = ImageWidget(self)
        self.MainLayout.addWidget(self.ImageWidget)
        self.ProgressBar = QtWidgets.QProgressBar(self)
        self.ProgressBar.setTextVisible(False)
        self.ProgressBar.setFixedHeight(10)
        self.MainLayout.addWidget(self.ProgressBar)

    """
        设置图像
        @param image QImage 格式图像
    """
    def setImage(self, image: QtGui.QImage) -> None:
        self.ImageWidget.setImage(image)

"""
    测试
"""
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = VideoWidget()

    imagePath = "../1.jpg"
    image = cv2.cvtColor(cv2.imread(imagePath), cv2.COLOR_BGR2RGB)
    height, width, channels = image.shape
    q_image = QtGui.QImage(image.data, width, height, channels * width, QtGui.QImage.Format_RGB888)

    test.setImage(q_image)

    test.show()
    sys.exit(app.exec_())