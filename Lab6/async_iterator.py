import asyncio

async def data_producer():  
    try:
        for i in range(1, 6):
            await asyncio.sleep(0.5)
            if i == 3:
                #Error simulation
                raise Exception("Read error")
            yield f"line {i}"
    except Exception as e:
        print(f"Error occurred: {e}")
        raise

#Consumer
async def main():
    try:
        async for line in data_producer():
            print(f"Processed: {line}")
    except Exception as e:
        print(f"Error occurred in main: {e}")

if __name__ == "__main__":
    asyncio.run(main())