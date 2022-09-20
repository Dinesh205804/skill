import requests

cookies = {
    '0ctf_csrf_cookie': '567607205187a2cf9f8c44400df7b65f',
    'ctf_session': 'f23686a4fb97a8551e7da0911e9868d7a68914da',
}

headers = {
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
}

data = {
    '0ctf_csrf_token': '567607205187a2cf9f8c44400df7b65f',
    'email': 'email@gmail.com',
    'password': 'dinesh',
}

response = requests.post('https://ctf.0ops.sjtu.cn/login', cookies=cookies, headers=headers, data=data)
print(response.text)
