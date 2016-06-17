import httplib
import json
import webob.dec
from webob import Response
from pprint import pprint


class Controller(object):
    def __init__(self):
        pass

    def index(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        response = Response(request=req, status=httplib.MULTIPLE_CHOICES,
                            content_type='application/json')
        if match['username'] == 'admin' and match['passwd'] == 'hitnslab':
            ans_str = 'login successfully'
            response.body = json.dumps(ans_str)
            response.status = '200 OK'
            response.set_cookie('token', '1846310132123', path='/', secure = False)
            print response.headers
            return response
        else:
            ans_str = 'bad username or passwd'
            response.body = json.dumps(ans_str)
            response.status = '200 OK'
            return response

    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)


def create_resource():
    return Controller()
