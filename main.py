import random
import time
from prometheus_client import start_http_server, Summary

# create a metric to track time spent to process request and number of requests made
REQUEST_TIME = Summary(name="request_processing_seconds", documentation="Time Spent Processing Requests")

# monitor the metric with a decorator
@REQUEST_TIME.time()
def process_request(t: float):
    """A dummy function to simulate delay"""
    time.sleep(t)



if __name__ == "__main__":
    print("Starting Server")
    # startup the server to expose the metrics
    start_http_server(8000)
    print("Server startup complete")

    # generate random requests
    while True:
        process_request(random.random())