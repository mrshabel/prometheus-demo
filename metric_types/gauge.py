import random
import time
from prometheus_client import start_http_server, Gauge


gauge = Gauge(name="number_of_saved_items", documentation="Total number of saved items")

items = set()

def measure_item_size(value: int):
    """Decrement gauge if value has been seen"""
    # set to initial size of items
    gauge.set(len(items))

    if value in items:
        items.remove(value)
        gauge.dec()
        pass
    
    # add to items and increment count
    items.add(value)
    gauge.inc()

    
if __name__ == "__main__":
    print("Starting Server")
    # startup the server to expose the metrics
    start_http_server(8000)
    print("Server startup complete")

    # generate random requests
    while True:
        val = random.randint(1, 10)

        print(f"Trying with {val}")

        measure_item_size(val)

        # sleep for 2 seconds
        time.sleep(2)