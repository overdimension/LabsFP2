def memoize(max_size=None, policy="LRU"):
    def decorator(func):
        cache = {}
        order = []

        def wrapper(*args):
            if args in cache:
                if policy == "LRU":
                    order.remove(args)
                    order.append(args)
                return cache[args]

            result = func(*args)

            if max_size and len(cache) >= max_size:
                if policy == "LRU":
                    oldest = order.pop(0)
                    cache.pop(oldest)

            cache[args] = result
            order.append(args)
            
            return result

        return wrapper
    return decorator