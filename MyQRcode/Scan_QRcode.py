from MyQRcode import QRCode

def Scan_qrcode():
    print("           Scan a QRcode            ")
    print("=====================================")
    print("1、请输入图片保存地址：")
    save_path = input('>>:').strip()
    results = QRCode.decode_qr_code(save_path)
    print("2、正在解码：")
    if len(results):
        print("解码结果是：")
        print(results[0].data.decode("utf-8"))
    else:
        print("Can not recognize.")

if __name__ == '__main__':
    Scan_qrcode()