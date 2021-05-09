import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_USER = "scrapy"
REDIS_PASS = "239dj+3kg8sk205nfbnsæ"

class RedisMixin:
    limit_404 = 20

    redis = redis.Redis(host=REDIS_HOST,
                        port=REDIS_PORT,
                        password=REDIS_PASS,
                        db=0,
                        decode_responses=True)

    def no_page_incrementer(self, key):
        self.redis.incr(key)

    def no_more_pages(self, key):
        value = self.redis.get(key)
        if value is not None:
            return int(value) > self.limit_404
        else:
            return False