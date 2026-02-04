from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI,Query
from client.rq_client import queue
from queues.worker import process_queue
app = FastAPI()

@app.get('/')
def root():
    return {'status': 'server is up and running'}

@app.post('/chat')
def chat(
        query:str = Query(..., description="the chat of the user")
):
   job = queue.enqueue(process_queue,query)
   return {"status" : "queued" ,'job_id': job.id}


@app.get('/job-status')
def get_result(
    job_id: str = Query(..., description="the job id")):
    job = queue.fetch_job(job_id)
    result = job.return_value()
    return {"status": result}