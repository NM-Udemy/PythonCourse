# core/file_manager.py
# ----------------------------
# ファイル操作ロジックをまとめる
# ----------------------------

import os
import shutil
from datetime import datetime


def get_files_with_dates(folder_path):
    """
    指定フォルダ内のファイル一覧と更新日付を取得する
    Returns: [(ファイル名, 更新日付文字列 "YYYYMMDD"), ...]
    """
    results = []
    for item in os.listdir(folder_path):
        file_path = os.path.join(folder_path, item)

        if os.path.isfile(file_path):
            mtime = os.path.getmtime(file_path)
            date_str = datetime.fromtimestamp(mtime).strftime("%Y%m%d")
            results.append((item, date_str))

    return results


def copy_files_by_date(folder_path):
    """
    ファイルを更新日付ごとのフォルダにコピーする

    Parameters
    ----------
    folder_path : str
        処理対象のフォルダパス
    """
    files = get_files_with_dates(folder_path)

    for name, date_str in files:
        src = os.path.join(folder_path, name)
        dest_folder = os.path.join(folder_path, date_str)
        dest = os.path.join(dest_folder, name)

        # 日付フォルダがなければ作成
        os.makedirs(dest_folder, exist_ok=True)

        # ファイルをコピー
        shutil.copy2(src, dest)

    return len(files)  # 処理したファイル数を返す
