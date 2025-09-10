# ui/main_window.py

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QFileDialog, QMessageBox
)
from PySide6.QtGui import QFont
from core.file_manager import copy_files_by_date  # ← 追加


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ファイル整理アプリ")
        self.setGeometry(200, 200, 500, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.path_display = QLineEdit()
        self.path_display.setPlaceholderText("ここに選択したフォルダのパスが表示されます")
        self.path_display.setFont(QFont("Arial", 12))
        layout.addWidget(self.path_display)

        self.select_button = QPushButton("フォルダ選択")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.run_button = QPushButton("実行")
        self.run_button.clicked.connect(self.run_processing)
        layout.addWidget(self.run_button)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "フォルダを選択")
        if folder_path:
            self.path_display.setText(folder_path)

    def run_processing(self):
        folder_path = self.path_display.text().strip()
        if not folder_path:
            QMessageBox.warning(self, "エラー", "先にフォルダを選択してください。")
            return

        try:
            count = copy_files_by_date(folder_path)
            QMessageBox.information(self, "完了", f"{count} 個のファイルを整理しました。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"処理中にエラーが発生しました:\n{e}")
