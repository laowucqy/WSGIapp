import routes
import wsgi
import add
import sub


class compute(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        add_resource = add.create_resource()
        sub_resource = sub.create_resource()
        mapper.connect("/add/{a}&{b}", controller=add_resource, action="getMessage",
                       conditions={'method': ['GET']})
        mapper.connect("/sub/{a}&{b}", controller=sub_resource, action="getMessage",
                       conditions={'method': ['GET']})
        super(compute, self).__init__(mapper)


