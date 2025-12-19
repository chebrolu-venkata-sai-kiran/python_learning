import threading

counter = 0

lock = threading.Lock()

def increment():
    global counter
    for _ in range(9):
        with lock:
            counter += 1

threads = [
    threading.Thread(target=increment) for _ in range(10)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")