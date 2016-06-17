import httplib
import json
import webob.dec
import MySQLdb
from webob import Response
from pprint import pprint
import uuid

class Controller(object):
    def __init__(self):
        pass

    def index(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        response = Response(request=req, status=httplib.MULTIPLE_CHOICES,
                            content_type='application/json')

        conn = MySQLdb.connect(host='localhost', user='root', passwd='hitnslab', db='user')
        cur = conn.cursor()
        sql = "select user_passwd from login where user_name= '%s'" % match['username']
        cur.execute(sql)
        result = cur.fetchone()
        print result
        print match['username']
        print match['passwd']
        if result[0] == match['passwd']:
            ans_str = 'login successfully'
            response.body = json.dumps(ans_str)
            response.status = '200 OK'
            token=str(uuid.uuid1())
            response.set_cookie('TOKEN', token, path='/', secure=False)
            fp = open("token.dat", 'a')
            fp.seek(0, 2)
            fp.write(token + '\n')
            fp.close()
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
