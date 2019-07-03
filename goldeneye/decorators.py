from prometheus_client import Histogram

from goldeneye.metrics import Metrics


def watchme(cls):
    if cls.__name__ not in Metrics.watched_objects:
        Metrics.watched_objects[cls.__name__] = {}

    for method in dir(cls):
        try:
            if callable(getattr(cls, method)) and not method.startswith('_'):
                hist = Histogram(f'{cls.__name__}_{method}_latency', f'Total latency of {cls.__name__}.{method}')
                Metrics.watched_objects[cls.__name__] = hist
                setattr(cls, method, hist.time()(getattr(cls, method)))
        except TypeError:
            print(f'Can not decorate {method}')
    return cls