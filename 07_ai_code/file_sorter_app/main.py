# main.py
# ----------------------------
# アプリのエントリーポイント
# ----------------------------

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

# アプリを起動するための処理
if __name__ == "__main__":
    app = QApplication(sys.argv)  # PySide6 のアプリケーションを作成
    window = MainWindow()         # メインウィンドウを作成
    window.show()                 # ウィンドウを画面に表示
    sys.exit(app.exec())          # アプリを実行（終了コードを返す）
