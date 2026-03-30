from async_map import sync_map

#Callback
def square(x):
    return x * x

#Async


#Test
def main():
    numbers = [1, 2, 3, 4, 5]

    #Callback
    print("Callback result:", sync_map(square, numbers))

if __name__ == "__main__":  main()
