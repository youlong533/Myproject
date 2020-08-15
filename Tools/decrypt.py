from Crypto.Cipher import AES
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations
from time import time
all_letters = ascii_letters + digits + '.,;'


class Decrypts:
    """base64 AES RSA 三种解密方法"""

    def __init__(self):
        # AES解密模式(须与加密模式一致）
        self.aes_mode = AES.MODE_ECB

    def base64_decry(ciphertext):
        """base64解密"""
        base64_decry = (base64.b64decode(ciphertext)).decode('utf-8')
        return base64_decry

    def aes_decrypt(self, encrypt_message, aes_key):
        """ AES解密
        :param encrypt_message: 密文
        :param aes_key: 秘钥
        :return: decrypt_text解密后内容
        """
        aes_mode = self.aes_mode
        aes = AES.new(key=aes_key, mode=aes_mode)
        decrypted_text = aes.decrypt(a2b_hex(encrypt_message))
        decrypted_text = decrypted_text.rstrip()  # 去空格
        return decrypted_text.decode()

    def rsa_decrypt(encrypt_msg_list, rsa_private_key):
        """ RSA解密
        :param encrypt_msg_list: 密文列表
        :param rsa_private_key: 私钥(字节类型)
        :return  解密后内容
        """
        random_generator = Random.new().read
        pri_key = RSA.importKey(rsa_private_key)
        cipher = Cipher_pkcs1_v1_5.new(pri_key)
        # 解密后信息列表
        msg_list = []
        for msg_str in encrypt_msg_list:
            msg_str = base64.decodebytes(msg_str)
            de_str = cipher.decrypt(msg_str, random_generator)
            msg_list.append(de_str.decode('utf-8'))
        return ''.join(msg_list)

    def md5_decrypt(md5_value):
        return




if __name__ == '__main__':
    str = Decrypts.base64_decry(b'5ri46b6Z')
    print(str)
    md5_value = 'be97741faab936ebcbcd12c4d72fe3f0'