import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("this lock is from  task 1 and with lock a")
        with lock_b:
            print("this lock is from  task 1 and with lock b")

def task2():
    with lock_b:
        print("this lock is from  task 2 and with lock b")
        with lock_a:
            print("this lock is from  task 2 and with lock a")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()
thread2.join()
thread1.join()