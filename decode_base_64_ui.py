import base64
import subprocess
from PyQt5 import QtWidgets, QtGui, QtCore
import json

class PDFConverterApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Conversor Base64 para PDF")
        self.setFixedWidth(800) 
        self.setFixedHeight(600) 
        self.base64_label = QtWidgets.QLabel("Base64 do PDF:")
        self.base64_input = QtWidgets.QPlainTextEdit()

        self.filename_label = QtWidgets.QLabel("Nome do arquivo de saída:")
        self.filename_input = QtWidgets.QLineEdit()

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setMaximum(100)

        self.convert_button = QtWidgets.QPushButton("Converter")
        self.convert_button.clicked.connect(self.convert_to_pdf)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.base64_label)
        layout.addWidget(self.base64_input)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.filename_input)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def convert_to_pdf(self):
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("Iniciando conversão")
        base64_data = self.base64_input.toPlainText()
        output_filename = self.filename_input.text()

        try:            
            self.progress_bar.setValue(25)
            self.progress_bar.setFormat("Decodificando o base64")
            QtCore.QCoreApplication.processEvents()
            decoded_data = base64.b64decode(base64_data)

            self.progress_bar.setValue(50)
            self.progress_bar.setFormat("Salvando o conteúdo em um arquivo PDF")
            QtCore.QCoreApplication.processEvents()
            with open(output_filename, 'wb') as pdf_file:
                pdf_file.write(decoded_data)

            self.progress_bar.setValue(75)
            self.progress_bar.setFormat("Abrindo o arquivo PDF")
            subprocess.Popen(["start", output_filename], shell=True)

            self.progress_bar.setValue(100)
            self.progress_bar.setFormat("Conversão concluída com sucesso!")
            QtCore.QCoreApplication.processEvents()
        except Exception as e:
            self.progress_bar.setFormat(f"Erro: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PDFConverterApp()
    window.show()
    app.exec_()
