from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'Hello World'

@app.route('/sayhello/<uname>')
def hello_user(uname):
   return '<h1>hey there %s</h1>' % uname

@app.route('/post/<int:num>')
def post(num):
   return '<h1>post number %s</h1>' % (num+1)

if __name__ == '__main__':
   app.run()