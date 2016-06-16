from pprint import pprint

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
        pprint(environ)
        if environ.get('REMOTE_USER') in self.req_usernames:
            return self.app(environ, start_response)
        start_response(
            '403 Forbidden', [('Content-type', 'text/html')])
        return ['You are forbidden to view this resource']



