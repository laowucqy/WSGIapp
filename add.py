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
        #pprint(req.environ)
        if "HTTP_COOKIE" in req.environ:
            print req.environ['HTTP_COOKIE']
        print req.cookies
        response = Response(request=req, status=httplib.MULTIPLE_CHOICES,
                            content_type='application/json')
        ans = int(match['a'])+int(match['b'])
        ans_str = match['a']+"+"+match['b']+"="+str(ans)
        response.body = json.dumps(ans_str)
        response.status ='200 OK'
        return response

    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)


def create_resource():
    return Controller()
