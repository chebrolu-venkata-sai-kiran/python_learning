import threading

counter = 0

def count_counter():
    global counter
    for _ in range(100_000_00):
        counter+=1
        
threads = [threading.Thread(target=count_counter) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("counter",counter)
