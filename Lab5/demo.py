from async_map import async_map_callback
import asyncio

#Callback
def square(x):
    return x * x

def callback_example():
    numbers = [1, 2, 3, 4, 5]
    def print_result(result):
        print("Callback result:", result)
    async_map_callback(numbers, square, print_result)


#Main
def main():
    callback_example()

if __name__ == "__main__":
    main()
