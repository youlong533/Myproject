import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set(1)
r.get()