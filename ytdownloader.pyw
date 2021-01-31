from __future__ import unicode_literals
from PyQt5.QtWidgets import QMessageBox
from youtube_dl import YoutubeDL
from PyQt5 import QtCore, QtGui, QtWidgets
import os
__author__ = "Tihanyi Marcell"


if not os.path.exists('Songs'):
    os.makedirs('Songs')

if not os.path.exists('Vids'):
    os.makedirs('Vids')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 100)
        MainWindow.setMaximumSize(QtCore.QSize(700, 100))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 10, 481, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(574, 10, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(574, 50, 91, 23))
        self.pushButton3.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.downloadmp3)
        self.pushButton2.clicked.connect(self.creator)
        self.pushButton3.clicked.connect(self.downloadmp4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindows", "YT Downloader MP3"))
        self.label.setText(_translate("MainWindow", "Link:"))
        self.pushButton.setText(_translate("MainWindow", "Download MP3"))
        self.pushButton2.setText(_translate("MainWindow", "Creator"))
        self.pushButton3.setText(_translate("MainWindow", "Download MP4"))

    def downloadmp3(self):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'Songs/%(title)s' + '.mp3',
            'noplaylist': True,
            'extract-audio': True,
        }
        link = self.plainTextEdit.toPlainText()
        video = link
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video, download=True)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_length = info_dict.get('duration')
            print("[convert] Converting Video to Audio file")
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("The song is downloaded into Songs folder! \n\n Song name : " + video_title)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()

    def downloadmp4(self):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'Vids/%(title)s' + '.mp4',
            'noplaylist': True,
            'extract-audio': True,
        }
        link = self.plainTextEdit.toPlainText()
        video = link
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video, download=True)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_length = info_dict.get('duration')
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("The video is downloaded into Vids folder! \n\n Video name : " + video_title)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()

    def creator(self):
        msg = QMessageBox()
        msg.setWindowTitle("Creator: TMarccci")
        msg.setText("Thanks for downloading!")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon("icon.ico"))
        x = msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
