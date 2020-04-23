#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from MyQR import myqr
from MyQRcode import QRCode

def myQRcode(content,icon_path):
    myqr.run(
        # 在命令后输入链接或者句子作为参数,然后在程序的当前目录中产生相应的二维码图片文件,默认命名为“qrcode.png”
        words=content,
        version=1,  # 设置容错率为最高默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H
        level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
        picture=icon_path,  # 用来将QR码图像与一张同目录下的图片相结合,产生一张黑白图片,格式可以是.jpg, .png, .bmp, .gif
        colorized=True,  # 可以使产生的图片由黑白(False)变为彩色(True)的
        contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
        brightness=1.0,  # 用来调节图片的亮度
        # save_name= save_path
    )

if __name__ == '__main__':
    print("           Make a QRcode            ")
    print("=====================================")
    print("1、请输入编码信息：")
    content = input('>>:').strip()
    print("2、请输入图片地址：")
    icon_path = input('>>:').strip()
    # print("3、请输入图片保存地址：")
    # save_path = input('>>:').strip()
    myQRcode(content,icon_path)
