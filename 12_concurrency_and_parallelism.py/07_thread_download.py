import threading
import requests
import time

def download(url):
    print(f"started downloading from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size : {len(resp.content)}")


urls = [
    "https://httpbin.org/image/svg",
    "https://httpbin.org/image"]

start_time = time.time()

threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Total time taken to download all the pages: {end_time - start_time} seconds")
