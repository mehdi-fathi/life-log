import redis


class App:
    redisHost = 'localhost'
    redisPort = 6379
    redisPassword = ''

    def __init__(self):
        self.selfredis = redis.Redis(
            host=self.redisHost,
            port=self.redisPort,
            password=self.redisPassword)
