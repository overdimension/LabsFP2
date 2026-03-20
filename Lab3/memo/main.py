from memoize import memoize

@memoize
def add(a, b):
    print("Calculating")
    return a + b

print(add(2, 3))
print(add(2, 3))