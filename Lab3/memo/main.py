from memoize import memoize

@memoize(max_size=2)
def square(x):
    print("Calculating...")
    return x * x

print(square(1))
print(square(2))
print(square(3))
print(square(1))