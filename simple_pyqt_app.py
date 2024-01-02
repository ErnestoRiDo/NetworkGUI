
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # Window setup
        self.setWindowTitle('Input Window')
        self.setGeometry(100, 100, 300, 200)

        # Layout setup
        layout = QVBoxLayout(self)

        # Input fields
        self.input1 = QLineEdit(self, placeholderText="Number of bots")
        layout.addWidget(self.input1)

        self.input2 = QLineEdit(self, placeholderText="Number of routers")
        layout.addWidget(self.input2)

        self.input3 = QLineEdit(self, placeholderText="Number of nodes")
        layout.addWidget(self.input3)

        # Submit button
        button = QPushButton('Submit', self)
        button.clicked.connect(self.onSubmit)
        layout.addWidget(button)

    def onSubmit(self):
        # Collect input values
        bots = self.input1.text()
        routers = self.input2.text()
        nodes = self.input3.text()

        # Output
        print(f"Bots: {bots}, Routers: {routers}, Nodes: {nodes}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
