from __future__ import annotations

from pathlib import Path
import shutil
from typing import Optional

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QLineEdit, QMessageBox
)

from core.analysis import (
    load_csv,
    compute_monthly_stats,
    compute_daily_mean,
    create_daily_trend_plot,
    export_to_excel,
    forecast_next_days,
    create_forecast_plot,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Stock Analysis & Forecast")

        self.csv_path_edit = QLineEdit(self)
        self.csv_path_edit.setPlaceholderText("Select input CSV (columns: date, price)")
        browse_btn = QPushButton("Browse CSV", self)
        browse_btn.clicked.connect(self.on_browse)

        run_btn = QPushButton("Run Analysis", self)
        run_btn.clicked.connect(self.on_run)

        save_png_btn = QPushButton("Save PNG...", self)
        save_png_btn.clicked.connect(self.on_save_png)

        save_excel_btn = QPushButton("Save Excel...", self)
        save_excel_btn.clicked.connect(self.on_save_excel)

        self.status_label = QLabel("", self)
        self.status_label.setWordWrap(True)

        top = QWidget(self)
        self.setCentralWidget(top)
        v = QVBoxLayout(top)

        h = QHBoxLayout()
        h.addWidget(self.csv_path_edit, 1)
        h.addWidget(browse_btn)
        v.addLayout(h)

        v.addWidget(run_btn)
        v.addWidget(save_png_btn)
        v.addWidget(save_excel_btn)
        v.addWidget(self.status_label)

        # Resolve directories relative to this file
        app_dir: Path = Path(__file__).resolve().parent.parent
        base_dir: Path = app_dir.parent
        self.default_outdir: Path = base_dir / "output"
        self.default_outdir.mkdir(parents=True, exist_ok=True)
        self.last_plot_path: Optional[Path] = None
        self.last_forecast_plot_path: Optional[Path] = None
        self.last_excel_path: Optional[Path] = None

    def on_browse(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
        if path:
            self.csv_path_edit.setText(path)

    def on_run(self) -> None:
        try:
            csv_path = Path(self.csv_path_edit.text()).expanduser()
            if not csv_path.exists():
                raise FileNotFoundError("CSV not found.")

            df = load_csv(csv_path)
            monthly = compute_monthly_stats(df)
            daily = compute_daily_mean(df)

            self.last_plot_path = create_daily_trend_plot(daily, self.default_outdir)

            # Forecast
            forecast_df = forecast_next_days(df, periods=30)
            self.last_forecast_plot_path = create_forecast_plot(df, forecast_df, self.default_outdir)

            # Excel
            excel_path = self.default_outdir / "analysis.xlsx"
            self.last_excel_path = export_to_excel(
                monthly_stats=monthly,
                daily_mean_df=daily,
                plot_image_path=self.last_plot_path,
                output_excel_path=excel_path,
                forecast_df=forecast_df,
                forecast_image_path=self.last_forecast_plot_path,
            )

            self.status_label.setText(
                f"Done.\nPNG: {self.last_plot_path}\nForecast PNG: {self.last_forecast_plot_path}\nExcel: {self.last_excel_path}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_save_png(self) -> None:
        if not self.last_plot_path or not self.last_forecast_plot_path:
            QMessageBox.information(self, "Info", "Please run analysis first.")
            return
        choice = QMessageBox.question(
            self,
            "Save which PNG?",
            "Save Daily Trend (Yes) or Forecast (No)?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
        )
        if choice == QMessageBox.StandardButton.Cancel:
            return
        src = self.last_plot_path if choice == QMessageBox.StandardButton.Yes else self.last_forecast_plot_path
        dst, _ = QFileDialog.getSaveFileName(self, "Save PNG As", str(src.name), "PNG Image (*.png)")
        if dst:
            shutil.copyfile(src, dst)
            self.status_label.setText(f"Saved PNG to: {dst}")

    def on_save_excel(self) -> None:
        if not self.last_excel_path:
            QMessageBox.information(self, "Info", "Please run analysis first.")
            return
        dst, _ = QFileDialog.getSaveFileName(self, "Save Excel As", "analysis.xlsx", "Excel Workbook (*.xlsx)")
        if dst:
            shutil.copyfile(self.last_excel_path, dst)
            self.status_label.setText(f"Saved Excel to: {dst}")


