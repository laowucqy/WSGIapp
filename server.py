import os
import sys
from paste import deploy
from wsgiref.simple_server import make_server
module_dir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir))
sys.path.insert(0, module_dir)
bind_host = "192.168.202.133"
bind_port = 8000


def server(app_name, conf_file):
    app = load_paste_app(app_name, conf_file)
    serve = make_server(bind_host, bind_port, app)
    serve.serve_forever()


def load_paste_app(app_name, conf_file):
    try:
        app = deploy.loadapp("config:%s" % os.path.abspath(conf_file), name=app_name)
        print app
        return app
    except(LookupError, ImportError) as e:
        raise RuntimeError(str(e))

if __name__ == '__main__':
    fp = open("token.dat", 'wb')
    fp.close()
    os.remove("token.dat")
    app_name = "main"
    conf_file = "laowuview.ini"
    server(app_name, conf_file)