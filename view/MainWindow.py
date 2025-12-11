from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create buttons
        pdf_btn = QPushButton("PDF")
        doc_btn = QPushButton("Docs")
        md_btn = QPushButton("Markdown")
        img_btn = QPushButton("Images")

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(pdf_btn)
        layout.addWidget(doc_btn)
        layout.addWidget(md_btn)
        layout.addWidget(img_btn)

        # Window config
        self.setWindowTitle("SarvaDocs")
        self.resize(800, 500)
        self.setLayout(layout)

        


class App:      # Main Application Wrapper
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        self.app.exec()


if __name__ == "__main__":
    application = App()
    application.run()
