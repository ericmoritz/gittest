from webob import Request, Response
from webob import exc
from webob.dec import wsgify
from routes.middleware import RoutesMiddleware
from routes import Mapper
import utils


@wsgify
def add(request):
    match = request.urlvars
    try:
        a, b = int(match['a']), int(match['b'])
    except Exception, e:
        raise exc.HTTPBadRequest(str(e))

    return Response(str(utils.add(a, b)), content_type="text/plain")


resources = {}
resources['add'] = add
mapper = Mapper()

mapper.connect(None, "/add/{a},{b}", resource="add")

@wsgify
def front(request):
    match = request.urlvars
    if match:
        resource = resources[match['resource']]

        return request.get_response(resource)
    else:
        raise exc.HTTPNotFound()

application = RoutesMiddleware(front, mapper)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server("", 8000, application)
    server.serve_forever()
