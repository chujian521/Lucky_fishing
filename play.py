# -*- encoding: utf-8 -*-
# @Time    : 2023/08/03 08:17:22
# @Author  : chujian521
# @File    : play.py

import os
import random
import subprocess
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QTimer, Qt, QUrl

class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("surprise!^_^!")
        self.setGeometry(100, 100, 800, 600)

        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.media_player.setVideoOutput(self.video_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_widget)

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        # Load and play the video on startup
        video_file = "test.avi"  # Replace with your video file name
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(video_file)))
        self.media_player.play()

        # Center the window and show fullscreen
        self.center_and_fullscreen()

        # Connect the mediaStatusChanged signal to exit the application
        self.media_player.mediaStatusChanged.connect(self.on_media_status_changed)

    def center_and_fullscreen(self):
        # Get the screen geometry
        screen = QDesktopWidget().screenGeometry()

        # Calculate the center position for the window
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2

        # Move the window to the center position
        self.move(x, y)

        # Show the window in fullscreen
        self.showFullScreen()

    def on_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            # Video has played to the end, exit the application
            self.close()

if __name__ == "__main__":
    if getattr(sys, 'frozen', False): 
        program_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    else:
        program_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(program_path)
    msg = ["恭喜你解锁了彩蛋^_^", "我们已经悄悄地获取了你设备的控制权", "骗你的，我们是公司安全管理部", "怎么？你信了？", "我们是冒充的公司安全管理部", "那现在你要做什么？", "不小心点开奇怪的文件当然要第一时间联系安全管理部！", "不要点击陌生文件", "不要将陌生U盘设备插入电脑", "保护数据安全人人有责"]
    app = QApplication(sys.argv)
    desktop = QApplication.desktop()
    screen_rect = desktop.screenGeometry(desktop.primaryScreen())
    width = screen_rect.width()
    height = screen_rect.height()

    if not os.path.exists("test.avi"):
        # Create and show the error box at the random position
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("错误")
        error_box.setText(os.getcwd())
        error_box.exec_()
    else:
        # Generate random position within the application window
        for i in range(len(msg)):
            rand_x = random.randint(100, width - 300)
            rand_y = random.randint(100, height- 300)

            # Create and show the error box at the random position
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setWindowTitle("错误")
            error_box.setText(msg[i])
            
            #error_box.setStandardButtons(QMessageBox.Ok)
            error_box.move(rand_x, rand_y)
            timer = QTimer()
            timer.timeout.connect(error_box.close)
            timer.start(random.randint(3000, 5000))
            error_box.exec_()
            if i == 1:
                try:
                    subprocess.Popen("taskmgr", shell=True)
                except subprocess.CalledProcessError:
                    pass
                time.sleep(2)
        player = VideoPlayerApp()
        player.show()
    sys.exit(app.exec_())