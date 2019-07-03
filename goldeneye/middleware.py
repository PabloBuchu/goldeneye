import gc

from goldeneye.metrics import Metrics
import objgraph


class MoneyPenny:
    def __init__(self, get_response):
        self.get_response = get_response

    @Metrics.TotalRequestTime.time()
    def __call__(self, request, *args, **kwargs):
        Metrics.RequestCounter.labels(method=request.method).inc()
        response = self.get_response(request, *args, **kwargs)
        Metrics.ResponseCounter.labels(response.status_code).inc()

        gc.collect()
        stats = objgraph.typestats()
        for obj, cnt in stats.items():
            Metrics.ObjectsInMemory.labels(obj).set(cnt)

        return response
