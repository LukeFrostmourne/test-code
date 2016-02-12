from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world ! welcome to use marathon v2'
    
@app.route('/version')
def print_version():
    return 'python3.5 flask0.10'

import optparse
def flaskrun(app, default_host="127.0.0.1", default_port="5000"):
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)
    options, _ = parser.parse_args()
    app.run(
        host=options.host,
        port=int(options.port)
    )

if __name__ == '__main__':
    flaskrun(app)
