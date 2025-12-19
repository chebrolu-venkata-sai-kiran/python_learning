import threading 
import time

def take_order():
    for i in range(1,5):
        print(f"Order {i} taken")
        time.sleep(2)
def brew_drink():
    for i in range(1,5):
        print(f"Drink {i} brewed")
        time.sleep(2)

#create threads
order_thread = threading.Thread(target=take_order)
order_thread.start()

brew_thread = threading.Thread(target=brew_drink)
brew_thread.start()

# wait for threads to finish
order_thread.join()
brew_thread.join()

print("All orders and drinks are done")

