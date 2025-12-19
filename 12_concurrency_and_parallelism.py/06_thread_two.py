import threading
import time

def prepare_drink(type_, wait_time ):
    print(f"{type_} drink: preparing...")
    time.sleep(wait_time)
    print(f"{type_} drink: prepared")

thread1 =threading.Thread(target=prepare_drink,args=("lemon", 2 ))
thread2 =threading.Thread(target=prepare_drink,args=("peach", 3 ))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
