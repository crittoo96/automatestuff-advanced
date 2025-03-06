"""
インターネット上からデータを取得するスクリプト

requestsを利用してExcelファイルをダウンロードする。
ダウンロードしたExcelファイルをdl_censuspopdata.xlsxとして保存する。
"""

import requests

# 直接ExcelファイルのURLを指定する
excel_link_url = "https://github.com/oreilly-japan/automatestuff2-ja/raw/refs/heads/main/ch13/censuspopdata.xlsx"

# requestsを利用してExcelファイルをダウンロードする
# quickWeather.pyを参考にする。
response = # ここに実装...
response.raise_for_status()

# ファイルを保存する。
# ここに実装...

print("dl_censuspopdata.xlsxをダウンロードしました。")
