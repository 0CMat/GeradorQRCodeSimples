# install pip
# install pip qrcode
# install  pip install pillow

import qrcode # importando o QRCode
from PIL import Image  # Importando o Image do PIL

img = qrcode.make('https://www.youtube.com/watch?v=wT7qyep-RGA')
img.save('borabill.png')

print('QRCode gerado com sucesso!')
