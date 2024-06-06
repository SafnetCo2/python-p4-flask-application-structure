#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'
@app.route('/<string:username>')
def user(username):
    return f'<h1>These profile is for {username}</h1>'

    
if __name__=='__main__':
    app.run()


@app.route('/')
def index():
    return '<h1>Welcome to the homepage!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=5555)

>>>>>>> fee8a5bb73ade7588138e1f2fed1f387fca5c449
