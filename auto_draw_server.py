from bottle import static_file
#from bottle import post
from bottle import get
from bottle import run


@get('/statics/<filepath:path>')
def server_statics(filepath):
    return static_file(filepath, root='statics/')


@get('/')
def index():
    return static_file('index.html', root='./')


run(port=8899, reloader=True, debug=True)


