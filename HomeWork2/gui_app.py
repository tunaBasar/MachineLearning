import os
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QFileDialog, QMessageBox, QTextEdit
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ultralytics import YOLO


class ObjectDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLOv8 Nesne Tespiti - Proje Ödevi 2")
        self.setGeometry(100, 100, 1200, 700)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, 'best.pt')

        try:
            self.model = YOLO(model_path)
            print(f"Model başarıyla yüklendi: {model_path}")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Model yüklenemedi!\nAranan Yol: {model_path}\n\nHata: {str(e)}")
            sys.exit()

        self.image_path = None
        self.original_image = None
        self.processed_image = None

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        panels_layout = QHBoxLayout()

        self.label_original = QLabel("Original Image")
        self.label_original.setAlignment(Qt.AlignCenter)
        self.label_original.setStyleSheet("border: 2px solid black; background-color: #f0f0f0;")
        self.label_original.setFixedSize(500, 500)

        self.label_tagged = QLabel("Tagged Image")
        self.label_tagged.setAlignment(Qt.AlignCenter)
        self.label_tagged.setStyleSheet("border: 2px solid black; background-color: #f0f0f0;")
        self.label_tagged.setFixedSize(500, 500)

        panels_layout.addWidget(self.label_original)
        panels_layout.addWidget(self.label_tagged)

        self.result_info = QTextEdit()
        self.result_info.setReadOnly(True)
        self.result_info.setMaximumHeight(100)
        self.result_info.setPlaceholderText("Tespit sonuçları ve sayıları burada listelenecek...")

        buttons_layout = QHBoxLayout()

        self.btn_select = QPushButton("Select Image")
        self.btn_select.clicked.connect(self.select_image)
        self.btn_select.setHeight = 40


        self.btn_test = QPushButton("Test Image")
        self.btn_test.clicked.connect(self.test_image)
        self.btn_test.setEnabled(False)

        self.btn_save = QPushButton("Save Image")
        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setEnabled(False)

        buttons_layout.addWidget(self.btn_select)
        buttons_layout.addWidget(self.btn_test)
        buttons_layout.addWidget(self.btn_save)

        main_layout.addLayout(panels_layout)
        main_layout.addWidget(self.result_info)
        main_layout.addLayout(buttons_layout)
        central_widget.setLayout(main_layout)

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Görsel Seç", "",
                                                   "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)", options=options)

        if file_path:
            self.image_path = file_path
            self.original_image = cv2.imread(file_path)

            self.display_image(self.original_image, self.label_original)

            self.btn_test.setEnabled(True)
            self.label_tagged.setText("Tagged Image")  # Reset
            self.label_tagged.setPixmap(QPixmap())  # Reset
            self.result_info.clear()

    def test_image(self):
        if self.image_path and self.model:
            results = self.model(self.image_path)

            self.processed_image = results[0].plot()

            self.display_image(self.processed_image, self.label_tagged)
            self.btn_save.setEnabled(True)

            class_names = results[0].names
            boxes = results[0].boxes
            class_counts = {}

            for box in boxes:
                cls_id = int(box.cls[0])
                cls_name = class_names[cls_id]
                class_counts[cls_name] = class_counts.get(cls_name, 0) + 1

            info_text = "Tespit Edilen Nesneler:\n"
            info_text += "-" * 30 + "\n"
            total_obj = 0
            for name, count in class_counts.items():
                info_text += f"• {name}: {count} adet\n"
                total_obj += count
            info_text += "-" * 30 + "\n"
            info_text += f"TOPLAM: {total_obj} nesne"

            self.result_info.setText(info_text)

    def save_image(self):
        if self.processed_image is not None:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Görüntüyü Kaydet", "result.jpg", "Images (*.jpg *.png)",
                                                       options=options)
            if file_path:
                cv2.imwrite(file_path, self.processed_image)
                QMessageBox.information(self, "Başarılı", "Görüntü başarıyla kaydedildi!")

    def display_image(self, img, label):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qt_image)
        label.setPixmap(pixmap.scaled(label.width(), label.height(), Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObjectDetectionApp()
    window.show()
    sys.exit(app.exec_())