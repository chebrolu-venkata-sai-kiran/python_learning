from multiprocessing import Process , Queue

def prepare_drink(queue):
    queue.put("drink is ready")

if __name__ == "__main__":
    drink_queue = Queue()
    drink_process = Process(target=prepare_drink, args=(drink_queue,))
    drink_process.start()
    drink_process.join()
    print(drink_queue.get())