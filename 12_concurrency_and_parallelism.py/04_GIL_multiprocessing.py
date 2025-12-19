from multiprocessing import Process
import time

def crunch_number():
    print(f"started counting numbers...")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"completed counting numbers...")

if __name__ =="__main__":
    #starting time 
    start_time = time.time()

    # Create two processes
    process1 = Process(target=crunch_number)
    process2 = Process(target=crunch_number)
    # Start the processes
    process1.start()
    process2.start()
    # Wait for both processes to finish
    process1.join()
    process2.join()
    # End time
    end_time = time.time()
    # Calculate total time taken
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")
