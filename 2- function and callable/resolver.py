import socket


class Resolver:
    _cache = {}

    def __inti__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def has_cache(self, host):
        if host in self._cache:
            return True
        return False

    def clear_cache(self):
        self._cache.clear()

resolver = Resolver()
print(resolver('google.com'))
print(resolver.has_cache('google.com'))
resolver.clear_cache()
print(resolver.has_cache('google.com'))