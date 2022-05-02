from utils.app import create_app
import time
from flask_cors import CORS
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
app = create_app()
CORS(app, supports_credentials=True)
@app.route('/')
def index():
    time.sleep(10)
    return 'hello world'
if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 9999),app)
    http_server.serve_forever()