import time

def sync_function():
    for i in range(3):
        time.sleep(1)
        print(f"Sync Function: {i}")

sync_function()
print("Sync Function Completed")
