from multiprocessing import Process
import time 

def cpu_heavy():
    print(f"crunching the numbers...")
    total = 0
    for i in range(10**9):
        total+=i
    print(f"completed crunching numbers... ")

if __name__ =='__main__':


    start = time.time()

    Processes = [Process(target=cpu_heavy) for _ in range(2)]

    [t.start() for t in Processes] 
    [t.join() for t in Processes]

    end = time.time()

    print(f"Execution time: {end - start} seconds")

