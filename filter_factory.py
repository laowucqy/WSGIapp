from pprint import pprint
import re
import os

import webob.dec


class filter_factory(object):
    def __init__(self, app):
        self.app = app

    @classmethod
    def factory(cls, global_conf, **kwargs):
        def filter(app):
            return cls(app)
        return filter


class filter01(filter_factory):
    def __init__(self, app):
        super(filter01, self).__init__(app)

    def __call__(self, environ, start_response):
        print 'request method is: %s' % environ['REQUEST_METHOD']
        return self.app(environ, start_response)

class filter02(filter_factory):
    def __init__(self, app):
        self.req_usernames = ['LAOWU']
        super(filter02, self).__init__(app)

    def __call__(self, environ, start_response):
        pattern = re.compile(r'/(\w+)/(\d+)&(\d+)')
        match = pattern.match(environ['PATH_INFO'])
        print len(match.groups())
        """if match.groups != 3:
            start_response(
                '403 Forbidden', [('Content-type', 'text/html')])
            return ['You are forbidden to view this resource']"""
        #print match.group(1,2,3)
        #pprint(environ)
        """if environ.get('REMOTE_USER') in self.req_usernames:"""
        print 'path_info is: %s' % environ['PATH_INFO']
        return self.app(environ, start_response)
        """start_response(
            '403 Forbidden', [('Content-type', 'text/html')])
        return ['You are forbidden to view this resource']"""


class filter03(filter_factory):
    def __init__(self, app):
        super(filter03, self).__init__(app)

    def __call__(self, environ, start_response):
        if "HTTP_COOKIE" in environ and os.path.exists("token.dat")==True :
            fp = open("token.dat", 'r')
            #print environ["HTTP_COOKIE"]
            for eachLine in fp:
                #print 'TOKEN=' + eachLine
                if 'TOKEN=' + eachLine[0:36] == environ["HTTP_COOKIE"]:
                    fp.close()
                    return self.app(environ, start_response)
            fp.close()
        start_response(
            '403 Forbidden', [('Content-type', 'text/html')])
        return ['please login']

class filter04(filter_factory):
    def __init__(self, app):
        super(filter04, self).__init__(app)

    #@webob.dec.wsgify
    def __call__(self, environ,start_response):
        return self.app(environ, start_response)





