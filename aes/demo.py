from Crypto.Cipher import AES
import base64

def add_to_16(par):
    par = par.encode() #先将字符串类型数据转换成字节型数据
    while len(par) % 16 != 0: #对字节型数据进行长度判断
        par += b'\x00' #如果字节型数据长度不是16倍整数就进行 补充
    return par

password = '5fd28e8b2d6c8678' #秘钥
text = '{"appid":"2","sec_level":"2","uid":0,"app_name":"jsd","idfa":"A0C8D591-F6D3-4FF6-9F82-ECD5C8BFE435","app_version":"5.4.0","channel":"AppStore","rongussd":"c45e664fd31c4166bfda3f803a44fde3","sys_version":"13.5","api_version":"2.0","platform":"ios","time_stamp":"1614920998","token":"bb528546e0ed88209ab01c1afca92024","device_id":"c45e664fd31c4166bfda3f803a44fde3","nettype":"WIFI","device_model":"iPhone12,3","version":"v540"}' #需要加密的内容
model = AES.MODE_ECB #定义模式
aes = AES.new(add_to_16(password),model) #创建一个aes对象

en_text = aes.encrypt(add_to_16(text)) #加密明文
print(en_text)
en_text = base64.encodebytes(en_text) #将返回的字节型数据转进行base64编码
print()
print(en_text)
en_text = en_text.decode('utf8') #将字节型数据转换成python中的字符串类型
print()
print(en_text.strip())
