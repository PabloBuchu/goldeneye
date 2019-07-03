from prometheus_client import Counter, Histogram, Gauge


class Metrics:
    RequestCounter = Counter(
        'http_requests_total', 'Total number of HTTP requests.',
        ['method']
    )
    ResponseCounter = Counter(
        'http_responses_total', 'Total number of HTTP responses',
        ['status_code']
    )
    TotalRequestTime = Histogram(
        'http_total_request_time', 'Total time of http request'
    )
    ObjectsInMemory = Gauge(
        'total_memory_objects', 'Total number of objects in memory',
        ['object_name']
    )

    watched_objects = {}
