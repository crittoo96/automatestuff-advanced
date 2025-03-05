import os
from datetime import datetime

try:
    import win32com.client
except ImportError:
    raise ImportError(
        "pywin32がインストールされていません。pywin32をインストールしてください。"
    )

print("Excelを使用してチャートを画像としてエクスポートしています...")
# Excelアプリケーションを起動
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False  # Excelウィンドウを非表示

# 絶対パスに変換

file_name = f'population-{datetime.now().strftime("%Y%m%d")}.xlsx'
abs_file_name = os.path.abspath(file_name)
wb_com = excel.Workbooks.Open(abs_file_name)

# 作成したシート名「Population」を取得
sheet_com = wb_com.Worksheets("Population")

# シート内のChartObjectsコレクションから最初のチャートを取得
# ※ openpyxlで追加したグラフはExcel上で「Chart 1」として扱われます
chart_object = sheet_com.ChartObjects(1)
# グラフをPNG形式でエクスポート（絶対パスを指定）
img_path = os.path.abspath("graph.png")
chart_object.Chart.Export(img_path, "PNG")

# Excelファイルを閉じ、Excelアプリケーションを終了
wb_com.Close(SaveChanges=False)
excel.Quit()

print(f"graph.pngとしてチャート画像をエクスポートしました。")
