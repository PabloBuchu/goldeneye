from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from werkzeug.wrappers import Response


def export(request):
    response = Response(
        generate_latest(),
    )
    response.headers['Content_Type'] = CONTENT_TYPE_LATEST

    return response
