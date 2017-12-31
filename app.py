from flask import Flask

app = Flask(__name__)

# @ signifies a decorator 
# a way to wrap a function and modify its behaviour
@app.route('/')
def index():
    return "Hello, World!"


@app.route('/about')
def about():
    return "<h1>About</h1>"

# e.g: http://localhost:5000/profile/Fred
@app.route('/profile/<user>')
def profile(user):
    return "Welcome %s" % user





if __name__ == '__main__':
    app.run(debug=True)

    