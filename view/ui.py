from PyQt6.QtWidgets import QMainWindow, QTreeView, QFormLayout, QLineEdit, QGraphicsView

class FormUI(QMainWindow):
    def __init__(self):
        super().__init__()
        form = QFormLayout()
        form.addRow("Say Something: ", QLineEdit())
        #todo

class ViewUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.treeView = QGraphicsView()
        self.setCentralWidget(self.treeView)
        #todo