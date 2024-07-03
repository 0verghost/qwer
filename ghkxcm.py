import sys
from PyQt5 import QtCore, QtWidgets, QtPrintSupport
from PyQt5.QtGui import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Final')
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.setGeometry(10, 40, 580, 280)
        self.editor.textChanged.connect(self.TextChanged)
        self.buttonOpen = QtWidgets.QPushButton('Open', self)
        self.buttonOpen.setGeometry(50, 350, 100, 40)
        self.buttonOpen.clicked.connect(self.Open)
        self.buttonOpen.setStyleSheet('background-color:#00416a')
        self.buttonOpen = QtWidgets.QShortcut(QKeySequence("F3"), self)
        self.buttonOpen.activated.connect(self.Open)
        self.setStyleSheet('background-color:#1d334a')
        self.editor.setStyleSheet('background-color: #5094d9')
        self.buttonSave = QtWidgets.QPushButton('Save', self)
        self.buttonSave.setGeometry(180, 350, 100, 40)
        self.buttonSave.clicked.connect(self.Save)
        self.buttonSave.setStyleSheet('background-color:#00406b')
        self.buttonSave = QtWidgets.QShortcut(QKeySequence("F5"), self)
        self.buttonSave.activated.connect(self.Save)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.setGeometry(460, 350, 110, 40)
        self.buttonPrint.clicked.connect(self.Print)
        self.buttonPrint.setStyleSheet('background-color:#1a4876')
        self.buttonPrint = QtWidgets.QShortcut(QKeySequence("F10"), self)
        self.buttonPrint.activated.connect(self.Print)
        self.TextChanged()
        self._createMenuBar()

    def _createMenuBar(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('&Open')
        open_menu = file_menu.addAction('&Open file', self.open_menu)
        file_save = menu.addMenu('&Save')
        view_menu = file_save.addAction('&Save file', self.save_menu)

    def Open(self):
        qp = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '','Text files (*.txt)')[0]
        if qp:
            file = QtCore.QFile(qp)
            if file.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(file)
                text = stream.readAll()
                self.editor.setPlainText(text)
                file.close()

    def Print(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def Save(self):
        save, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', "txt file (*.txt)")
        text = self.editor.toPlainText()
        if save:
            with open(save, 'w') as file:
                file.write(text)

    def TextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)

    def open_menu(self):
        qop = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt)')[0]
        if qop:
            fiile = QtCore.QFile(qop)
            if fiile.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(fiile)
                text = stream.readAll()
                self.editor.setPlainText(text)
                fiile.close()

    def save_menu(self):
        saave, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', "txt file (*.txt)")
        texxt = self.editor.toPlainText()
        if saave:
            with open(saave, 'w') as file:
                file.write(texxt)

App = QtWidgets.QApplication(sys.argv)
window = Window()
window.resize(600, 400)
window.show()
sys.exit(App.exec_())


