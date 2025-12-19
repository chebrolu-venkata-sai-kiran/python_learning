import threading
import time

def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk is boiled.")

def bake_bread():
    print("Baking bread...")
    time.sleep(3)
    print("Bread is baked.")

start = time.time()

# Create threads
thread1 = threading.Thread(target=boil_milk)
thread2 = threading.Thread(target=bake_bread)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish

thread1.join()
thread2.join()

# Calculate total time taken

end = time.time()

total_time = end - start

print(f"Total time taken: {total_time:.2f} seconds")

