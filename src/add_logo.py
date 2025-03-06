"""
画像の右下にロゴを追加するスクリプト

予め用意したlogo.pngを、画像の右下に追加する。
ch19/resizeAndAddLogo.pyを参考にして作成しました。
"""

import os

from PIL import Image

# ロゴ画像のファイル名を指定
LOGO_FILENAME = "logo.png"

# ロゴ画像を開く
logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

# ロゴをつけた画像の出力先ディレクトリの指定
# ここに実装...

# カレントディレクトリの全画像をループする
for filename in os.listdir("."):
    if (
        not (filename.endswith(".png") or filename.endswith(".jpg"))
        or filename == LOGO_FILENAME
    ):
        continue
    img = Image.open(filename)

    # ロゴを貼られる側（グラフ画像）の画像のサイズを取得
    width, height = img.size

    print(f"ロゴを追加中 {filename}...")

    # ロゴを追加する
    # ここに実装...

    # ロゴを付けた画像を別画像として保存
    # ここに実装...

    print(f"{filename}にロゴを追加完了しました。")
    print(f"出力先: {SAVE_DIR}/{filename}")
