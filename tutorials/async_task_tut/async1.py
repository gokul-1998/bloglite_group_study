import asyncio

async def async_function():
    for i in range(3):
        await asyncio.sleep(1)
        print(f"Async Function: {i}")

async def main():
    await asyncio.gather(async_function(), async_function(), async_function())

asyncio.run(main())
print("Async Functions Completed")
