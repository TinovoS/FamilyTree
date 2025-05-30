import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QSplitter
from view.ui import ViewUI, FormUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FamilyTree")
        self.resize(1440, 900)

        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        form_ui = FormUI()
        view_ui = ViewUI()
        main_splitter.addWidget(form_ui)
        main_splitter.addWidget(view_ui)

        main_splitter.setSizes([400, 1200])
        self.setCentralWidget(main_splitter)
        #todo

    def show_tree_view(self):
        #todo
        self.central_stack.setCurrentIndex(0)
        #self.view_ui.update_tree()

    def show_form_view(self, person_id = None):
        #todo
        #if person_id:
        #    self.form_ui.load_person_data(person_id)
        self.central_stack.setCurrentIndex(0)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()