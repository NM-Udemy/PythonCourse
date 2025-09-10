# main.py
# ----------------------------
# 電卓アプリの入口
# main_window.py の MainWindow を呼び出す
# ----------------------------

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow   # 追加：自作MainWindowを読み込む

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
