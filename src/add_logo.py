"""
予め用意したlogo.pngを、画像の右下に追加する

ch19/resizeAndAddLogo.pyを参考にして作成しました。
"""

import os
from PIL import Image

LOGO_FILENAME = 'logo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

SAVE_DIR = 'withLogo'
os.makedirs(SAVE_DIR, exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)

    # ロゴを貼られる側の画像のサイズを取得
    width, height = im.size

    print(f'ロゴを追加中 {filename}')

    # ロゴの余白を設定
    logo_padding_width, logo_padding_height = 10, 10
    
    # ロゴを張り付ける
    im.paste(logo_im, (width-logo_width-logo_padding_width, height-logo_height-logo_padding_height), logo_im)

    im.save(os.path.join(SAVE_DIR, filename))


