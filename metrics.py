from prometheus_client import Counter, start_wsgi_server
import random
import time

counter = Counter(name="http_requests_total", documentation="Total number of HTTP requests in the system", labelnames=["endpoint", "method"])

# define labels here to enforce it since the values are loaded on runtime
counter.labels(endpoint="/check", method="GET")
counter.labels(endpoint="/check", method="POST")
counter.labels(endpoint="/visit", method="GET")
counter.labels(endpoint="/visit", method="POST")

def simulate_requests(endpoint: str, method: str):
    """A dummy function to simulate a request to the server"""
    # increment counter here
    counter.labels(endpoint=endpoint, method=method).inc()


if __name__ == "__main__":
    server, thread = start_wsgi_server(8000)
    print("Metrics server running on http://localhost:8000")

    # simulate random requests
    while True:
        endpoint, method = random.choice(["/check", "/visit"]), random.choice(["GET", "POST"])
        simulate_requests(endpoint=endpoint, method=method)
        # sleep for 1 second
        time.sleep(1)

    