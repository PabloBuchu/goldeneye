import gc
import http
import objgraph

from werkzeug.wrappers import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from goldeneye.metrics import Metrics


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


class MMetricsMiddleware:
    def __init__(self, app, *args, **kwargs):
        self.app = app
        super(MProxyMiddleware, self).__init__(*args, **kwargs)

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if path == '/metrics':
            return Response(generate_latest(),
                            content_type=CONTENT_TYPE_LATEST,
                            status=http.HTTPStatus.OK)(environ, start_response)

        return self.app(environ, start_response)
