import datetime,hashlib,base64
str_t = 'shaChecksum-'+ datetime.datetime.now().strftime("%Y%m%d%H%M")[0:11] +'-leuny7AY'
sha_str = hashlib.sha256(str_t.encode('utf-8')).digest()
b64_str = str(base64.b64encode(sha_str),encoding = "utf-8")[0:6]
print(b64_str)