from prometheus_client import Counter, start_wsgi_server, Histogram
import random
import time

requests_total = Counter(name="http_requests_total", documentation="Total number of HTTP requests in the system", labelnames=["endpoint", "method", "status"])
requests_latency = Histogram(name="http_requests_latency_seconds", documentation="Latency of HTTP requests in the system in seconds", labelnames=["endpoint", "method", "status"], buckets=[.05, .1, .5, 1.0, 1.5])

# define labels here to enforce it since the values are loaded on runtime
# requests_total.labels(endpoint="/check", method="GET")
# requests_total.labels(endpoint="/check", method="POST")
# requests_total.labels(endpoint="/visit", method="GET")
# requests_total.labels(endpoint="/visit", method="POST")
# requests_total.labels(endpoint="/log", method="GET")
# requests_total.labels(endpoint="/log", method="POST")


def simulate_requests(endpoint: str, method: str, status: str, latency: float):
    """
        A dummy function to simulate a request to the server

        Parameters:
            endpoint(str): The request endpoint
            method(str): The HTTP method that was used
            status(str): The status of the request
            latency(str): The request latency
    """
    # increment requests total counter
    requests_total.labels(endpoint=endpoint, method=method, status=status).inc()

    # simulate delay and record latency here
    with requests_latency.labels(endpoint=endpoint, method=method, status=status).time():
        time.sleep(latency)



if __name__ == "__main__":
    server, thread = start_wsgi_server(8000)
    print("Metrics server running on http://localhost:8000")

    # label tags
    endpoints = ["/check", "/visit", "/log"]
    methods = ["GET", "POST", "PATCH"]
    statuses = ["200", "400", "404", "500"]

    # simulate random requests
    while True:
        endpoint, method, status = random.choice(endpoints), random.choice(methods), random.choice(statuses)
        # select latency from a random distribution. (0.1 seconds to 1.5 seconds)
        latency = random.uniform(0.1, 1.5)

        # simulate request
        simulate_requests(endpoint=endpoint, method=method, status=status, latency=latency)
        # sleep for 0.5 seconds
        time.sleep(0.5)

    