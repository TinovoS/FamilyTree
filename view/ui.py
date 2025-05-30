from PyQt6.QtWidgets import QMainWindow, QTreeView, QFormLayout, QLineEdit, QGraphicsView, QWidget, QVBoxLayout, QLabel, \
    QPushButton


class FormUI(QWidget):
    def __init__(self):
        super().__init__()

        form_layout = QFormLayout()

        form_layout.addRow(QLabel("<b>Personal Information</b>"))
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.birth_date = QLineEdit()
        self.death_date = QLineEdit()

        form_layout.addRow("First Name:", self.first_name)
        form_layout.addRow("Last Name:", self.last_name)
        form_layout.addRow("Birth Date:", self.birth_date)
        form_layout.addRow("Death Date:", self.death_date)

        form_layout.addRow(QLabel("<b>Relationships</b>"))
        self.parents = QLineEdit()
        self.spouses = QLineEdit()
        self.children = QLineEdit()

        form_layout.addRow("Parents:", self.parents)
        form_layout.addRow("Spouses:", self.spouses)
        form_layout.addRow("Children:", self.children)

        form_layout.addRow(QLabel("<b>Actions</b>"))
        self.save_btn = QPushButton("Save Person")
        self.clear_btn = QPushButton("Clear Form")
        form_layout.addRow(self.save_btn)
        form_layout.addRow(self.clear_btn)

        self.setLayout(form_layout)

        self.setStyleSheet("""
                    QWidget {
                        padding: 15px;
                        border-right: 1px solid #dee2e6;
                    }
                    QFormLayout QLabel {
                        background: transparent;
                        color: #495057;
                    }
                    QLabel[text^="<b>"] {
                        font-weight: bold;
                        margin-top: 15px;
                        color: #495057;
                    }
                """)

        self.save_btn.clicked.connect(self.save_person)
        self.clear_btn.clicked.connect(self.clear_form)

    def save_person(self):
        print("Saving person:", self.first_name.text(), self.last_name.text())

    def clear_form(self):
        self.first_name.clear()
        self.last_name.clear()
        self.birth_date.clear()
        self.death_date.clear()
        self.parents.clear()
        self.spouses.clear()
        self.children.clear()


class ViewUI(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.treeView = QGraphicsView()
        layout.addWidget(self.treeView)
        #todo