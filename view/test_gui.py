from PySide6.QtWidgets import *

app = QApplication()

window = QWidget()
window.setWindowTitle("SarvaDocs")
window.resize(800,500)


layout = QHBoxLayout()

pdf_btn = QPushButton("PDF")
layout.addWidget(pdf_btn)

docs_btn = QPushButton("Docs")
layout.addWidget(docs_btn)

window.setLayout(layout)
window.show()
app.exec()
