def memoize(max_size=None):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]

            result = func(*args)

            if max_size and len(cache) >= max_size:
                first_key = list(cache.keys())[0]
                cache.pop(first_key)

            cache[args] = result
            return result

        return wrapper
    return decorator