from multiprocessing import Process
import time

def worker(task):
    print(f"Worker process {task} started")
    time.sleep(1)
    print(f"Worker process {task} finished")

if __name__ == "__main__":
    team_workers = [
        Process(target=worker,args = (f"working #{i}",))
        for i in range(1,5)
    ]
    print(f"tasks started")
    for i in team_workers:
        i.start()
    
    for i in team_workers:  
        i.join()
    print(f"tasks finished")