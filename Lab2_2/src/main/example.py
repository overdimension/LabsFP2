from modules.generator import fib_generator

n = 10
print(f"First {n} Fibonacci numbers:")
for num in fib_generator(n):
    print(num)