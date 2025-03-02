import random
import time
from prometheus_client import start_http_server, Counter


counter = Counter(name="app_failures", documentation="Total number of exceptions")


def exceptions_counter(value: int):
        time.sleep(2)
        try:
            if value != 7:
                raise ValueError(f"Expected 7 but received {value}")
        except ValueError:
            counter.inc()
        
if __name__ == "__main__":
    print("Starting Server")
    # startup the server to expose the metrics
    start_http_server(8000)
    print("Server startup complete")

    # generate random requests
    while True:
        rand_value = random.randint(1, 10)
        print(f"Trying with {rand_value}")
        exceptions_counter(rand_value)