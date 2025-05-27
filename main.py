import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from view.ui import ViewUI, FormUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FamilyTree")
        self.resize(1024, 768)

        self.central_stack = QStackedWidget()
        self.setCentralWidget(self.central_stack)

        self.form_ui = FormUI()
        self.view_ui = ViewUI()

        self.central_stack.addWidget(self.form_ui)
        self.central_stack.addWidget(self.view_ui)
        #todo
        #self.show_tree_view()

    def show_tree_view(self):
        #todo
        self.central_stack.setCurrentIndex(0)
        #self.view_ui.update_tree()

    def show_form_view(self, person_id = None):
        #todo
        #if person_id:
        #    self.form_ui.load_person_data(person_id)
        self.central_stack.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()