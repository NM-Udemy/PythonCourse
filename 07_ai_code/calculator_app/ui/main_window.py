# ui/main_window.py

from PySide6.QtWidgets import (
    QMainWindow, QLineEdit, QVBoxLayout, QWidget,
    QPushButton, QGridLayout
)
from PySide6.QtGui import QFont
from functools import partial
from core.calculator import calculate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("電卓アプリ")
        self.setGeometry(100, 100, 300, 400)

        self._just_calculated = False  # ← 新しく追加（計算直後フラグ）

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # --- 表示欄 ---
        self.display = QLineEdit("0")
        self.display.setFont(QFont("Arial", 24))
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        # --- ボタン配置 ---
        button_layout = QGridLayout()
        layout.addLayout(button_layout)

        # 数字ボタン
        numbers = [
            (7, 0, 0), (8, 0, 1), (9, 0, 2),
            (4, 1, 0), (5, 1, 1), (6, 1, 2),
            (1, 2, 0), (2, 2, 1), (3, 2, 2),
            (0, 3, 1)
        ]
        self._add_buttons(numbers, button_layout, self.num_pressed)

        # 演算子ボタン
        operators = [
            ("+", 0, 3), ("-", 1, 3),
            ("×", 2, 3), ("÷", 3, 3)
        ]
        self._add_buttons(operators, button_layout, self.operator_pressed)

        # 特殊ボタン
        button_layout.addWidget(self._make_button("C", self.clear_display), 3, 0)
        button_layout.addWidget(self._make_button("=", self.calculate_result), 3, 2)

    # ----------------------------
    # ボタン生成
    # ----------------------------
    def _make_button(self, text, slot):
        button = QPushButton(text)
        button.setFont(QFont("Arial", 18))
        button.clicked.connect(partial(slot, text))
        return button

    def _add_buttons(self, items, layout, slot):
        for text, row, col in items:
            layout.addWidget(self._make_button(str(text), slot), row, col)

    # ----------------------------
    # ボタンの処理
    # ----------------------------
    def num_pressed(self, num):
        current = self.display.text()

        if self._just_calculated:
            # 計算直後に数字を押したらリセットして再入力
            self.display.setText(str(num))
            self._just_calculated = False
        elif current == "0":
            self.display.setText(str(num))
        else:
            self.display.setText(current + str(num))

    def operator_pressed(self, operator):
        current = self.display.text()

        if self._just_calculated:
            # 計算直後に演算子を押したら、その結果を使って続行
            self._just_calculated = False

        if current[-1] in "+-×÷":
            current = current[:-1]
        self.display.setText(current + operator)

    def clear_display(self, _=None):
        self.display.setText("0")
        self._just_calculated = False

    def calculate_result(self, _=None):
        expression = self.display.text()
        result = calculate(expression)
        self.display.setText(result)
        self._just_calculated = True  # ← 計算直後フラグを立てる
