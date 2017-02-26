#!/user/bin/env python
import json
import falcon
import os
import mimetypes
from wsgiref import simple_server

config = json.load(open('./serverConfig.json'))

dummy_data = {
    'employees': [
        {
            'name': 'Tom',
            'age': 24,
            'title': 'front end developer'
        },
        {
            'name': 'Jerry',
            'age': 29,
            'title': 'designer'
        }
    ],
    'customers': [
        {
            'name': 'Angela',
            'age': 25,
            'balance': 400
        },
        {
            'name': 'Steve',
            'age': 49,
            'balance': 240
        }
    ]
}

class Customers:
    def on_get(self, req, res):
        path = req.path
        res.status = falcon.HTTP_200
        customers = dummy_data['customers']
        res.body = json.dumps([customers])

class Employees:
    def on_get(self, req, res):
        path = req.path
        res.status = falcon.HTTP_200
        employees = dummy_data['employees']
        res.body = json.dumps([employees])

def serve_file(filepath, res, req):
    if os.path.isfile(filepath):
        content_type = mimetypes.guess_type(filepath)[0]
        file_type = content_type.split('/')[0]
        res.content_type = content_type
        res.status = falcon.HTTP_200
        if file_type == 'image':
            res.stream = open(filepath, 'rb')
            res.stream_len = os.path.getsize(filepath)
        else:
            with open(filepath, 'r') as text_file:
                res.body = text_file.read()
    else:
        res.status = falcon.HTTP_404

def static(req, res):
    path = req.path.lstrip('/')
    serve_file(path, res, req)

class Index:
    def __init__(self, index_file='index.html'):
        self.index_file = index_file

    def on_get(self, req, res):
        if req.path == '/':
            path = self.index_file
        else:
            path = req.path
        serve_file(path, res, req)

def init_server():
    app = falcon.API()
    return app

def add_routes(app):
    app.add_route('/customers', Customers())
    app.add_route('/employees', Employees())
    app.add_sink(static, '/dist')
    app.add_route('/', Index())
    return app

def start_server(app, config):
    host = config['host']
    port = config['port']
    httpd = simple_server.make_server(host, port, app)
    print(f'Serving on {host}:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    app = init_server()
    app = add_routes(app)
    start_server(app, config)
