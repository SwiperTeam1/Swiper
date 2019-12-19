import random

import requests

from common import keys
from swiper import config


def gen_vcode(size=4):
    start = 10 ** (size - 1)
    end = 10 ** size - 1
    return random.randint(start, end)


def send_sms(phone):
    params = config.YZX_PARAMS.copy()
    params['mobile'] = phone
    vcode = keys.VCODE_KEY %(phone)
    params['param'] = gen_vcode()
    resp = requests.post(config.YZX_URL, json=params)

    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return
    else:
        return '访问出错'
