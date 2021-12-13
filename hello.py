from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = prompt('Enter Username')
    return 'hello world'

@app.route('/ay/')
def ay():
    return 'The ay project page'

@app.route('/about')
def about():
    return 'The about page'




if __name__ == '__main__':
    app.run()


