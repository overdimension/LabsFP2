import asyncio

async def data_producer():  
    for i in range(1, 6):
        await asyncio.sleep(0.5)
        if i == 3:
            #Error simulation
            raise Exception("Read error at line 3")
        yield f"line {i}"

#Consumer
async def main():
    async for line in data_producer():
        print(f"Processed: {line}")

if __name__ == "__main__":
    asyncio.run(main())