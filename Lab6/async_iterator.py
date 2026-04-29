import asyncio

#Producer
async def data_producer():  
    try:
        for i in range(1, 11):
            await asyncio.sleep(0.3)
            if i == 7:
                raise Exception("Read error")
            yield f"Data chunk {i}"
    except Exception as e:
        raise e

async def data_processor_batched(batch_size=3, filter_func=None):
    batch = []
    
    async for item in data_producer():
        #Filtration
        if filter_func and not filter_func(item):
            print(f"Filtered out: {item}")
            continue
        
        batch.append(item)
        
        if len(batch) >= batch_size:
            print(f"Processing batch: {batch}")
            batch = [] 
            
    if batch:
        print(f"Processing leftovers: {batch}")

#Consumer
async def main():
    try:
        #Filtered: only odd chunks will be processed
        await data_processor_batched(
            batch_size=3,
            filter_func=lambda x: int(x.split()[-1]) % 2 == 1
        )
    except Exception as e:
        print(f"Error occurred in main: {e}")

if __name__ == "__main__":
    asyncio.run(main())