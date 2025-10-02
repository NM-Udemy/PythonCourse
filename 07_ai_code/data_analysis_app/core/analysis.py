from __future__ import annotations

from pathlib import Path
from typing import Tuple, Optional

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from xgboost import XGBRegressor


def load_csv(csv_path: Path) -> pd.DataFrame:
    """Load the CSV file with UTF-8 encoding and parse date/price columns.

    Assumes columns: date (YYYY-MM-DD), price (float-like).
    """
    df: pd.DataFrame = pd.read_csv(csv_path, encoding="utf-8")
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="raise")
    df["price"] = pd.to_numeric(df["price"], errors="raise")
    return df


def compute_monthly_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Compute monthly mean, max, median, and min for price.

    Returns a DataFrame with columns: month, mean, max, median, min
    where month is in YYYY-MM format.
    """
    grouped = df.groupby(df["date"].dt.to_period("M"))["price"]
    stats: pd.DataFrame = grouped.agg(mean="mean", max="max", median="median", min="min").reset_index()
    stats["month"] = stats["date"].astype(str)
    stats = stats[["month", "mean", "max", "median", "min"]]
    return stats


def compute_daily_mean(df: pd.DataFrame) -> pd.DataFrame:
    """Compute daily mean of price.

    Returns a DataFrame with columns: date (Timestamp), mean
    """
    daily: pd.DataFrame = (
        df.groupby(df["date"].dt.to_period("D"))["price"].mean().reset_index()
    )
    daily["date"] = daily["date"].dt.to_timestamp()
    daily = daily.rename(columns={"price": "mean"})
    return daily


def create_daily_trend_plot(daily_mean_df: pd.DataFrame, output_dir: Path, filename: str = "daily_trend.png") -> Path:
    """Create and save a line plot of daily average price over time.

    Returns the path to the saved image.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path: Path = output_dir / filename

    plt.figure(figsize=(10, 4))
    plt.plot(daily_mean_df["date"], daily_mean_df["mean"], color="tab:blue", linewidth=1.8)
    plt.title("Daily Average of price")
    plt.xlabel("Date")
    plt.ylabel("Average price")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    return output_path


def export_to_excel(
    monthly_stats: pd.DataFrame,
    daily_mean_df: pd.DataFrame,
    plot_image_path: Path,
    output_excel_path: Path,
    forecast_df: Optional[pd.DataFrame] = None,
    forecast_image_path: Optional[Path] = None,
) -> Path:
    """Export analysis tables and plots to an Excel file using XlsxWriter.

    - Sheet "MonthlyStats": monthly statistics table
    - Sheet "DailyTrend": daily mean table
    - Sheet "Forecast" (optional): forecast table
    - Sheet "Charts": embedded images
    """
    output_excel_path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(output_excel_path, engine="xlsxwriter") as writer:
        monthly_stats.to_excel(writer, sheet_name="MonthlyStats", index=False)
        daily_mean_df.to_excel(writer, sheet_name="DailyTrend", index=False)
        if forecast_df is not None:
            forecast_df.to_excel(writer, sheet_name="Forecast", index=False)

        workbook = writer.book
        charts_ws = workbook.add_worksheet("Charts")
        writer.sheets["Charts"] = charts_ws
        charts_ws.insert_image("B2", str(plot_image_path))
        if forecast_image_path is not None:
            charts_ws.insert_image("B22", str(forecast_image_path))

    return output_excel_path


def prepare_daily_series(df: pd.DataFrame) -> pd.Series:
    """Create a daily frequency series of price with forward-filled gaps.

    Assumes df contains columns: date (Timestamp), price (float-like).
    """
    daily = (
        df.set_index("date")["price"]
        .sort_index()
        .asfreq("D")
        .ffill()
    )
    return daily


def forecast_next_days(df: pd.DataFrame, periods: int = 30) -> pd.DataFrame:
    """Forecast next N days of price using XGBoost with lag/rolling features.

    Returns DataFrame with columns: date, forecast
    """
    series = prepare_daily_series(df)

    def compute_features(values: list[float]) -> dict[str, float]:
        n = len(values)
        def lag(k: int) -> float:
            return values[-k] if n >= k else values[-1]
        def rmean(k: int) -> float:
            k = min(k, n)
            return float(np.mean(values[-k:]))
        def rstd(k: int) -> float:
            k = min(k, n)
            return float(np.std(values[-k:], ddof=0))
        feats = {
            "lag_1": lag(1),
            "lag_2": lag(2) if n >= 2 else lag(1),
            "lag_5": lag(5) if n >= 5 else rmean(min(5, n)),
            "lag_10": lag(10) if n >= 10 else rmean(min(10, n)),
            "ma_5": rmean(5),
            "ma_10": rmean(10),
            "ma_20": rmean(20),
            "std_5": rstd(5),
            "std_10": rstd(10),
            "std_20": rstd(20),
        }
        return feats

    # Build training frame from historical series
    values = list(map(float, series.values.tolist()))
    rows: list[dict[str, float]] = []
    targets: list[float] = []
    for i in range(20, len(values)):
        hist = values[: i]
        feats = compute_features(hist)
        rows.append(feats)
        targets.append(values[i])
    X = pd.DataFrame(rows)
    y = pd.Series(targets)

    model = XGBRegressor(
        n_estimators=500,
        learning_rate=0.05,
        max_depth=5,
        subsample=0.9,
        colsample_bytree=0.9,
        reg_lambda=1.0,
        objective="reg:squarederror",
        random_state=42,
        n_jobs=0,
    )
    model.fit(X, y)

    # Recursive multi-step forecasts
    future_dates = pd.date_range(series.index[-1] + pd.Timedelta(days=1), periods=periods, freq="D")
    preds: list[float] = []
    hist_values = values.copy()
    for _ in range(periods):
        feats = compute_features(hist_values)
        x_next = pd.DataFrame([feats])
        yhat = float(model.predict(x_next)[0])
        preds.append(yhat)
        hist_values.append(yhat)

    forecast_df: pd.DataFrame = pd.DataFrame({"date": future_dates, "forecast": preds})
    return forecast_df


def create_forecast_plot(df: pd.DataFrame, forecast_df: pd.DataFrame, output_dir: Path, filename: str = "forecast.png") -> Path:
    """Create an overlay plot of historical price and forecast.

    Returns the path to the saved image.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path: Path = output_dir / filename

    hist = df.sort_values("date")
    plt.figure(figsize=(10, 4))
    plt.plot(hist["date"], hist["price"], color="tab:blue", linewidth=1.5, label="History")
    plt.plot(forecast_df["date"], forecast_df["forecast"], color="tab:orange", linewidth=1.8, linestyle="--", label="Forecast (+30D)")
    plt.title("Price Forecast (Next 30 Days)")
    plt.xlabel("Date")
    plt.ylabel("price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    return output_path


