from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 260)
    w.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())


