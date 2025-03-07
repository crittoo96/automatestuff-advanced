"""
インターネット上からデータを取得するスクリプト

requestsを利用してExcelファイルをダウンロードする。
ダウンロードしたExcelファイルをdl_censuspopdata.xlsxとして保存する。
"""

import requests


def run():

    # 直接ExcelファイルのURLを指定する
    excel_link_url = "https://github.com/oreilly-japan/automatestuff2-ja/raw/refs/heads/main/ch13/censuspopdata.xlsx"

    # requestsを利用してExcelファイルをダウンロードする
    # quickWeather.pyを参考にする。
    response = requests.get(excel_link_url)
    response.raise_for_status()

    # ファイルを保存する。
    with open("dl_censuspopdata.xlsx", "wb") as file:
        # ファイルの書き込み
        file.write(response.content)

    print("dl_censuspopdata.xlsxをダウンロードしました。")


if __name__ == "__main__":
    run()
