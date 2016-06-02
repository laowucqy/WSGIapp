import routes
import wsgi
import versions
import sayhello
import username


class API(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
            print mapper
        versions_resource = versions.create_resource()
        sayhello_resource = sayhello.create_resource()
        username_resource = username.create_resource()
        mapper.connect("/images/", controller=versions_resource, action="index")
        mapper.connect("/text/", controller=sayhello_resource, action="index")
        mapper.connect("/username/{id}", controller=username_resource, action="getMessage", conditions={'method': ['GET']})
        super(API, self).__init__(mapper)

