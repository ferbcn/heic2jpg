import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QMainWindow, QLabel, QComboBox
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from heic2jpg import convert_folder_heic2jpg

output_file_types = ['jpg', 'png']


class MainWindowWidget(QWidget):

    def __init__(self):
        super().__init__()

        QMainWindow.__init__(self, None, QtCore.Qt.WindowType.WindowStaysOnTopHint)

        self.message = "<b>Drop</b> your files <b>here</b>"
        self.output_file_format = 'jpg'

        # set position
        self.setGeometry(0, 0, 200, 200)
        self.setWindowTitle('HEIC Image Converter ')

        # background
        self.icon = QLabel(self)
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon.setPixmap(QPixmap('icon_s.png'))

        self.comboBox = QComboBox(self)
        for item in output_file_types:
            self.comboBox.addItem(item)
        self.comboBox.activated.connect(self.set_output_file_format)

        self.message = QLabel(self)
        self.message.setMinimumWidth(200)
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message.setText("<b>Drop</b> your files <b>here</b>")

        # A Vertical layout to include the button layout and then the image
        layout = QVBoxLayout()
        layout.addWidget(self.icon)
        layout.addWidget(self.message)
        layout.addWidget(self.comboBox)
        self.setLayout(layout)

        # Enable dragging and dropping onto the GUI
        self.setAcceptDrops(True)

        self.show()

    def set_output_file_format(self, format):
        self.output_file_format = output_file_types[format]
        print("Output file format set to:", self.output_file_format)

    # The following three methods set up dragging and dropping for the app
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        # Drop files directly onto the widget
        if e.mimeData().hasUrls:
            e.accept()
            for url in e.mimeData().urls():
                folder_path = str(url.toLocalFile())
            print(folder_path)
            # is it file or folder
            is_folder = True
            if is_folder:
                # run conversion
                convert_folder_heic2jpg(folder_path, self.output_file_format)
        else:
            e.ignore()


# Run if called directly
if __name__ == '__main__':
    # Initialise the application
    app = QApplication(sys.argv)
    # Call the widget
    ex = MainWindowWidget()
    sys.exit(app.exec())
