import requests
import json
import logging


logger = logging.getLogger(__name__)


RPC_USER = 'drivenet_user'
RPC_PW = 'drivenet_pw'


def call(method, params={}):
    url = f'http://{RPC_USER}:{RPC_PW}@localhost:8332/'
    headers = {
        'content-type': 'application/json',
    }

    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return response.json()
