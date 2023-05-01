"""
여러 개의 QR코드를 한 번에 생성하는 코드 만들고 실행
"""

import qrcode

file_path = '01_10/04.QR코드_생성기/qr코드모음.txt';
with open(file_path, 'rt', encoding='UTF8') as f :
  read_lines = f.readlines()
  
  for line in read_lines:
    line = line.strip()
    print(line)
    
    qr_data = line
    qr_img = qrcode.make(qr_data)
    
    save_path = f'01_10/04.QR코드_생성기/{qr_data}.png'
    qr_img.save(save_path)