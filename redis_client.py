import redis

redis_client = redis.Redis("localhost", 6379, 0)

redis_client.set("message", 10)
print(int(redis_client.get("message")))

redis_client.close()
