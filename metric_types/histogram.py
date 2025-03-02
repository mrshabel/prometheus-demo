import random
import time
from prometheus_client import start_http_server, Histogram


histogram = Histogram(name="request_latency", documentation="Request Latency (Seconds)")

@histogram.time()
def process_request(delay: float):
    """A dummy function to simulate delay"""
    time.sleep(delay)



if __name__ == "__main__":
    print("Starting Server")
    # startup the server to expose the metrics
    start_http_server(8000)
    print("Server startup complete")

    # generate random requests
    while True:
        delay = random.random()
        process_request(delay)