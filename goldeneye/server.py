from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response, Request


def application():
    response = Response('Hello World!', mimetype='text/plain')
    return response


class Shortly(object):
    def dispatch_request(self, request):
        return Response(generate_latest(), content_type=CONTENT_TYPE_LATEST)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    app = Shortly()
    return app


run_simple('127.0.0.1', 5001, create_app())
