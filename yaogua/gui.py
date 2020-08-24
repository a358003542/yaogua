#!/usr/bin/env python
# -*-coding:utf-8-*-


import sys

from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtCore import QUrl
from pkg_resources import resource_filename
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QWidget, QMainWindow, QApplication, \
    QMessageBox

from yaogua import __version__
from yaogua import yaogua_rc


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__()
        self.parent = parent

        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.webview = QWebEngineView()
        self.webpage = QWebEnginePage()
        self.webview.setPage(self.webpage)
        url = QUrl.fromLocalFile(
            resource_filename("yaogua", "html_resource/zhou_yi_yao_gua.html"))
        self.webview.load(url)

        mainLayout.addWidget(self.webview)


class YaoGuaApp(QMainWindow):
    def __init__(self, app=None):
        super().__init__()
        self.app = app

        self.initUi()

    def initUi(self):
        self.setMinimumSize(800, 700)
        self.center()
        self.setWindowTitle('周易预测')
        self.setWindowIcon(QIcon(':/app.png'))

        self.mywidget = MyWidget(self)
        self.setCentralWidget(self.mywidget)

        self.show()

    def about(self):
        QMessageBox.about(self, "关于本程序", f"周易预测小程序 version: {__version__}")

    # center method
    def center(self):
        screen = self.app.screens()[0]
        screen_size = screen.size()
        size = self.geometry()
        self.move((screen_size.width() - size.width()) / 2, \
                  (screen_size.height() - size.height()) / 2)


def main():
    app = QApplication(sys.argv)

    yaogua_app = YaoGuaApp(app)

    yaogua_app.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
