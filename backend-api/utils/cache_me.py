import time


class CacheMe:
    def __init__(self, ttl, not_found_obj=None):
        self.ttl = ttl
        self.cache = {}
        self.not_found_obj = not_found_obj

    def set(self, key, value):
        self.cache[key] = {"value": value, "time": time.time()}

    def get(self, key):
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry["time"] < self.ttl:
                return entry["value"]
            else:
                del self.cache[key]
        return self.not_found_obj
