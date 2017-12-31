from flask import Flask, request, render_template

app = Flask(__name__)

# @ signifies a decorator 
# a way to wrap a function and modify its behaviour
# http://localhost:5000/
@app.route('/')
def index():
    return "Hello, World!"

# e.g: http://localhost:5000/profile/Fred
@app.route('/profile/<user>')
def profile(user):
    return render_template("profile.html", user=user)

