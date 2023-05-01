"""
QR코드 생성 코드 만들고 실행
다음의 코드는 www.naver.com의 qr코드를 생성하는 프로그램
qr코드 생성기는 단순하게 문자를 qr코드로 변환하기 때문에 어떠한 문자라도 가능하다
"""

import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = '01_10/04.QR코드_생성기/' + qr_data + '.png'
qr_img.save(save_path)