import redis

r = redis.StrictRedis()
pool = redis.ConnectionPool(host = "", port =, db =)
