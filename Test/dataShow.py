import sys
import time
sys.path.append("../")

from Service.DataShow import DataShow
from Service.DataLoad import DataLoad
import Main
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageDisplayWidget(QWidget):
    def __init__(self, image):
        super().__init__()
        self.setWindowTitle("OpenCV 图像显示")
        self.resize(800, 600)

        # 创建 QLabel 用于显示图像
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # 创建布局并添加 QLabel
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # 显示图像
        self.display_image(image)

    def display_image(self, image):
        # 将 QImage 转换为 QPixmap 并显示
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

S = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Small"
L = "D:\\vscode\\code\\item_vscode\\Badminton\\DataMarker\\Test\\TestData\\Large"

if __name__ == "__main__":

    loadService = DataLoad(Main.MODEL_DICT)
    showService = DataShow(Main.MODEL_DICT)
    bef = time.time()
    loadService.loadData(L)


    # 创建 PyQt 应用
    app = QApplication(sys.argv)

    # 创建窗口并显示图像
    window = ImageDisplayWidget(showService.getVideoQImage(15000))
    print(time.time() - bef)
    window.show()

    # 运行 PyQt 应用
    sys.exit(app.exec_())

