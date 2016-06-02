import httplib
import json
import webob.dec
from webob import Response


class Controller(object):
    def __init__(self):
        self.text = "hellow world"

    def index(self, req):
        response = Response(request=req, status=httplib.MULTIPLE_CHOICES, content_type='application/json')
        response.body = json.dumps(dict(text=self.text))
        return response

    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)


def create_resource():
    return Controller()
