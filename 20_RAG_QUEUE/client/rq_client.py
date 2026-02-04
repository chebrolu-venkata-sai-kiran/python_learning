from redis import Redis
from rq import Queue

# Connect to Redis

queue = Queue(connection=Redis(
    host='localhost',
    port=6379
   
))

# queue.enqueue(process_queue, args=(arg1, arg2,...))