from memoize import memoize

@memoize(max_size=2, policy="LFU")
def square(x):
    print(f"Calculating square of {x}...")
    return x * x

print(square(1))  # freq: 1 -> 1
print(square(2))  # freq: 2 -> 1
print(square(1))  # freq: 1 -> 2
print(square(3))  # freq: 3 -> 1 # Evicts 2 (LFU) since it has the lowest frequency (1) compared to 1 (2) and 3 (1)