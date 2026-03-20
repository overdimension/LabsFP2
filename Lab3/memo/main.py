from memoize import memoize

@memoize(max_size=2, policy="LRU")
def square(x):
    print(f"Calculating square of {x}...")
    return x * x

print(square(1))
print(square(2))
print(square(1))
print(square(3))