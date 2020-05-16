#simple.py
_version__ = '0.1.0'

import re
import requests

URL = 'https://www.google.com'

def do_hello():
    result = requests.get(URL)
    print(re.findall('<title>(.*?)</title>', result.text)[0])

if __name__ == '__main__':
    do_hello()