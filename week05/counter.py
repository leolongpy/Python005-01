import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)


def counter(video_id):
    r.hincrby("video_count",video_id,amount=1)
    return r.hget("video_count",video_id)


print(counter(1))
print(counter(1))
print(counter(1))
print(counter(2))
