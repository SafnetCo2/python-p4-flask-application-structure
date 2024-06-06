from flask import Flask
practice=Flask(__name__)

@practice.route('/')
def hello_world():
    return '<p> Hello world</p>'


if __name__=='__main__':
    practice.run(debug=True,port=5555)
    