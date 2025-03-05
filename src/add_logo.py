"""
予め用意したlogo.pngを、画像の右下に追加する

ch19/resizeAndAddLogo.pyを参考にして作成しました。
"""

import os

from PIL import Image

LOGO_FILENAME = "logo.png"

logo_img = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_img.size

# ロゴをつけた画像の出力先ディレクトリの指定
SAVE_DIR = "withLogo"
os.makedirs(SAVE_DIR, exist_ok=True)

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

    # ロゴの余白を設定
    logo_padding_width, logo_padding_height = 10, 10

    # ロゴを張り付ける
    img.paste(
        logo_img,
        (
            width - logo_width - logo_padding_width,
            height - logo_height - logo_padding_height,
        ),
        logo_img,
    )

    # ロゴを付けた画像を別画像（-with-logo）として保存
    no_extension_filename = os.path.splitext(filename)[0]
    img.save(os.path.join(SAVE_DIR, f"{no_extension_filename}-with-logo.png"))

    print(f"{filename}にロゴを追加完了しました。")
    print(f"出力先: {SAVE_DIR}/{filename}")
