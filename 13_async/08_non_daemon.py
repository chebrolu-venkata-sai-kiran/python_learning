import threading
import time

def monitoring():
    while True:
        time.sleep(1)
        print("monitoring temperature 🌡️")

t = threading.Thread(target=monitoring,daemon= False)
t.start()
time.sleep(3)
print("main completed")