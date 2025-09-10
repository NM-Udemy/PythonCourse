# core/calculator.py
# ----------------------------
# 電卓の計算処理だけを担当するモジュール
# UI とは分離してシンプルに保つ
# ----------------------------

def calculate(expression: str) -> str:
    """文字列の数式を計算して結果を返す（整数専用）"""
    try:
        # UIで使う「×」「÷」をPythonの演算子に変換
        expression = expression.replace("×", "*").replace("÷", "//")

        # eval は危険なので、本来はパーサーを作るべきだが
        # 今回は初心者向けにシンプルに使う（整数だけ）
        result = eval(expression)

        return str(result)

    except ZeroDivisionError:
        return "エラー: 0で割れません"
    except Exception:
        return "エラー"
