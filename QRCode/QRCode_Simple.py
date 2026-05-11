# install pip
# install pip qrcode
# install  pip install pillow

import qrcode # importando o QRCode
from PIL import Image  # Importando o Image do PIL

img = qrcode.make('https://api.whatsapp.com/send/?phone=5571988504374&text&type=phone_number&app_absent=0')
img.save('whatsapp aldo.png')

print('QRCode gerado com sucesso!')
