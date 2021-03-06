from flask import Flask, request, render_template

app = Flask(__name__)

# @ signifies a decorator 
# a way to wrap a function and modify its behaviour
# http://localhost:5000/
@app.route('/')
def index():
    return "Hello, World!"

# http://localhost:5000/about
@app.route('/about')
def about():
    return "<h1>About</h1>"

# e.g: http://localhost:5000/profile/Fred
@app.route('/profile/<user>')
def profile(user):
    return "Welcome %s" % user


# e.g: using template: http://localhost:5000/profile/Fred
@app.route('/profile/<user>')
def profile(user):
    return render_template("profile.html", user=user)


# e.g: http://localhost:5000/post/8594
@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post ID = %s" % post_id

# e.g: http://localhost:5000/http
@app.route('/http', methods=['GET', 'POST'])
def http():
    if request.method == "POST":
        return "POST method detected"
    else:
        return "GET method detected"




if __name__ == '__main__':
    app.run(debug=True)

    