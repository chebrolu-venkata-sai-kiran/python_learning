# GIL Global Interpreter lock

# Mutex is a locking system using in the python

# if 1 thread touches the value they get the mutex if a theard having the mutex next thread will be unable to access the value 
# and change the value 

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing. ")

thread1 = threading.Thread(target=brew_chai,name="barista")
thread2 = threading.Thread(target=brew_chai,name="barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken: {end - start} seconds")
