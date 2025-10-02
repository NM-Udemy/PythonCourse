from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple, List

from core.analysis import (
    load_csv,
    compute_monthly_stats,
    compute_daily_mean,
    create_daily_trend_plot,
    export_to_excel,
    forecast_next_days,
    create_forecast_plot,
)


def resolve_default_paths(script_path: Path) -> tuple[Path, Path, Path]:
    """Resolve default input/output paths relative to the executing file.

    Returns a tuple of (csv_path, output_dir, excel_path).
    """
    app_dir: Path = script_path.parent
    base_dir: Path = app_dir.parent  # points to 07_ai_code
    csv_path: Path = base_dir / "data" / "sample.csv"
    output_dir: Path = base_dir / "output"
    excel_path: Path = output_dir / "analysis.xlsx"
    return csv_path, output_dir, excel_path


def main(argv: List[str] | None = None) -> int:
    script_path: Path = Path(__file__).resolve()
    default_csv, default_outdir, default_excel = resolve_default_paths(script_path)

    parser = argparse.ArgumentParser(
        description=(
            "Read sample.csv, compute monthly stats (mean/max/median/min) for price, "
            "plot daily average trend, forecast next 30 days, and export results to Excel."
        )
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=default_csv,
        help="Path to input CSV file (default: app-relative 07_ai_code/data/sample.csv)",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=default_outdir,
        help="Directory to save outputs (default: 07_ai_code/output)",
    )
    parser.add_argument(
        "--excel",
        type=Path,
        default=default_excel,
        help="Path to output Excel file (default: 07_ai_code/output/analysis.xlsx)",
    )

    args = parser.parse_args(argv)

    df = load_csv(args.csv)
    monthly_stats = compute_monthly_stats(df)
    daily_mean = compute_daily_mean(df)

    plot_path = create_daily_trend_plot(daily_mean, args.outdir)

    # Forecast next 30 days
    forecast_df = forecast_next_days(df, periods=30)
    forecast_plot_path = create_forecast_plot(df, forecast_df, args.outdir)

    export_to_excel(
        monthly_stats,
        daily_mean,
        plot_path,
        args.excel,
        forecast_df=forecast_df,
        forecast_image_path=forecast_plot_path,
    )

    print(f"Loaded CSV: {args.csv}")
    print(f"Monthly stats rows: {len(monthly_stats)}")
    print(f"Daily trend rows: {len(daily_mean)}")
    print(f"Plot saved: {plot_path}")
    print(f"Forecast rows: {len(forecast_df)}")
    print(f"Forecast plot saved: {forecast_plot_path}")
    print(f"Excel saved: {args.excel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


