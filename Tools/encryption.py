import hashlib
import os
from Crypto.Cipher import AES
import base64
from binascii import b2a_hex
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


class Encrypts:
    """MD5 base64 AES RSA 四种加密方法"""

    def __init__(self):
        self.aes_mode = AES.MODE_ECB  # AES加密模式
        self.aes_key_size = 256  # AES秘钥，随机数值
        self.rsa_count = 2048  # RSA秘钥对，随机数值

    def md5_encrypt(plaintext):
        """ MD5加密
        :param plaintext: 需要加密的内容
        :return: encrypt_str密文
        """
        h1 = hashlib.md5()  # 创建md5对象
        h1.update(plaintext.encode(encoding='utf-8'))  # 必须声明encode
        # 加密
        encrypt_str = h1.hexdigest()
        return encrypt_str

    def base64_encry(plaintext):
        """base64加密"""
        base64_encry = base64.b64encode(plaintext.encode('utf-8'))
        return base64_encry

    def generate_aes_key(self):
        """AES秘钥生成"""
        # length for urandom
        key_size = self.aes_key_size
        u_len = int(key_size / 8 / 4 * 3)
        aes_key = base64.b64encode(os.urandom(u_len))  # os.urandom()生成随机字符串
        return aes_key

    def aes_encrypt(self, message, aes_key):
        """use AES to encrypt message,
        :param message: 需要加密的内容
        :param aes_key: 密钥
        :return: encrypted_message密文
        """
        mode = self.aes_mode  # 加密模式
        if type(message) == str:
            message = bytes(message, 'utf-8')
        if type(aes_key) == str:
            aes_key = bytes(aes_key, 'utf-8')
        # aes_key, message必须为16的倍数
        while len(aes_key) % 16 != 0:
            aes_key += b' '

        while len(message) % 16 != 0:
            message += b' '
        # 加密对象aes
        aes = AES.new(key=aes_key, mode=mode)
        encrypt_message = aes.encrypt(plaintext=message)
        return b2a_hex(encrypt_message)

    def generate_rsa_keys(self):
        """RSA秘钥对生成"""
        rsa_count = self.rsa_count
        # 随机数生成器
        random_generator = Random.new().read
        # rsa算法生成实例
        rsa = RSA.generate(rsa_count, random_generator)
        # master的秘钥对的生成
        rsa_public_key = rsa.publickey().exportKey()
        rsa_private_key = rsa.exportKey()
        return rsa_public_key, rsa_private_key

    def rsa_encrypt(message, rsa_public_key):
        """use RSA to encrypt message,
        :param message: 需要加密的内容
        :param rsa_public_key: 公钥(字节类型）
        :return: encrypt_msg_list密文列表
        """
        pub_key = RSA.importKey(rsa_public_key)
        # 加密对象
        cipher = Cipher_pkcs1_v1_5.new(pub_key)
        msg = message.encode('utf-8')
        # 分段加密
        default_encrypt_length = 245
        length = default_encrypt_length
        msg_list = [msg[i:i + length] for i in list(range(0, len(msg), length))]
        # 加密后信息列表
        encrypt_msg_list = []
        for msg_str in msg_list:
            cipher_text = base64.b64encode(cipher.encrypt(message=msg_str))
            encrypt_msg_list.append(cipher_text)
        return encrypt_msg_list

if __name__ == '__main__':
    str = Encrypts.md5_encrypt("游龙")
    print(str)
