from PyQt5.QtCore import Qt, QCoreApplication, QThread, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, \
    QWidget, QPushButton, QFileDialog, QMessageBox

from pyqt_image_to_text.listWidget import FileListWidget
from pyqt_image_to_text.scripts import saveImage

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
QApplication.setFont(QFont('Arial', 12))


class Thread(QThread):
    runFinished = pyqtSignal(str, bool)

    def __init__(self, src, dst):
        super().__init__()
        self.__src = src
        self.__dst = dst

    def run(self):
        try:
            saveImage(self.__src, self.__dst)
            self.runFinished.emit(self.__dst, True)
        except Exception as e:
            self.runFinished.emit(str(e), False)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Image to Text')

        self.__topWidget = FileListWidget()

        self.__saveBtn = QPushButton('Save')
        self.__saveBtn.clicked.connect(self.__save)
        self.__saveBtn.setEnabled(False)

        self.__topWidget.itemUpdate.connect(self.__saveBtn.setEnabled)

        lay = QVBoxLayout()
        lay.addWidget(self.__topWidget)
        lay.addWidget(self.__saveBtn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __save(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            src = self.__topWidget.getDir()
            dst = directory
            self.__t = Thread(src, dst)
            self.__t.start()
            self.__saveBtn.setEnabled(False)
            self.__t.runFinished.connect(self.__informComplete)

    def __informComplete(self, text, f):
        informDialog = QMessageBox(self)
        if f:
            title = 'Finished!'
            message = f'Open {text} to see the result!'
        else:
            title = 'Error!'
            message = text
        informDialog.setWindowTitle(title)
        informDialog.setText(message)
        informDialog.exec()
        self.__saveBtn.setEnabled(True)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())