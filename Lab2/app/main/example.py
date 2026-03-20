from app.modules.generator import fib_generator

def main():
    n = 10
    print(f"First {n} Fibonacci numbers:")
    for num in fib_generator(n):
        print(num)