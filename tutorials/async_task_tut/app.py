import asyncio

async def fetch_data_from_server():
    print("Fetching data... (This may take a moment)")

    # Simulate a delay (e.g., a network request) using asyncio.sleep
    await asyncio.sleep(2)

    # Simulated data retrieval
    data = "Data received from the server"

    return data

async def main():
    # Calling the async function and awaiting the result
    data = await fetch_data_from_server()
    print(f"Received data: {data}")

if __name__ == "__main__":
    # Create an event loop and run the async function
    asyncio.run(main())
