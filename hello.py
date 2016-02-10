from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world ! welcome to use marathon v2'
    
@app.route('/version')
def print_version():
    return 'python3.5 flask0.10'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
