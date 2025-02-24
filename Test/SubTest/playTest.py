import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer, Qt


class VideoPlayer(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("简易视频播放器")
        self.resize(800, 600)
        self.video_path = video_path
        self.cap = cv2.VideoCapture(self.video_path)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.is_playing = False

        self.init_ui()

    def init_ui(self):
        # 创建 QLabel 用于显示视频帧
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        # 创建播放和暂停按钮
        self.play_button = QPushButton("播放", self)
        self.play_button.clicked.connect(self.play_video)

        self.pause_button = QPushButton("暂停", self)
        self.pause_button.clicked.connect(self.pause_video)

        # 创建布局并添加组件
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.play_button)
        layout.addWidget(self.pause_button)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # 将 OpenCV 图像转换为 QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

            # 将 QImage 转换为 QPixmap 并显示
            pixmap = QPixmap.fromImage(q_image)
            self.label.setPixmap(pixmap)
        else:
            self.pause_video()  # 如果视频结束，暂停播放

    def play_video(self):
        if not self.is_playing:
            self.timer.start(30)  # 设置定时器间隔（ms），根据视频帧率调整
            self.is_playing = True
            self.play_button.setText("继续")

    def pause_video(self):
        self.timer.stop()
        self.is_playing = False
        self.play_button.setText("播放")

    def closeEvent(self, event):
        self.cap.release()  # 释放视频捕获对象
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_path = "D:\\vscode\\code\\item_vscode\\Badminton\\SensorSteamService\\Test\\VideoTest\\output.avi" #  替换为你的视频文件路径
    player = VideoPlayer(video_path)
    player.show()
    sys.exit(app.exec_())