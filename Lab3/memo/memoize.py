def memoize(max_size=None, policy="LRU"):
    def decorator(func):
        cache = {}
        order = []
        freq = {}

        def wrapper(*args):
            if args in cache:
                freq[args] += 1
                if policy == "LRU":
                    order.remove(args)
                    order.append(args)
                return cache[args]

            result = func(*args)

            if max_size and len(cache) >= max_size:
                if policy == "LRU":
                    key_to_remove = order.pop(0) 
                elif policy == "LFU":
                    key_to_remove = min(freq, key=freq.get)
                    if key_to_remove in order:
                        order.remove(key_to_remove)
                
                cache.pop(key_to_remove)
                freq.pop(key_to_remove)

            cache[args] = result
            order.append(args)
            freq[args] = 1

            return result

        return wrapper
    return decorator