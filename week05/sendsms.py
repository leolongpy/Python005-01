import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
def sendsms(telephone_number, content):
    num = r.get(f'telnum_{telephone_number}')
    if num and int(num) > 5:
        print('发送失败，请一分钟后重试')
    else:
        print(content)
        r.incrby(f'telnum_{telephone_number}', amount=1)
        if not num:
            r.expire('telnum',60)


sendsms(18810636797,'hello')