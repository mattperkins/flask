from flask import Flask, request, render_template

app = Flask(__name__)


# http://localhost:5000/
# create routes with a conditional statement in profile.html template
@app.route('/')
@app.route('/<user>')

# set variable to none by default
def index(user=None):
    return render_template("profile.html", user=user)


@app.route('/cart')
def cart():
    fruit = ["Lemon", "Lime", "Banana", "Peach", "Melon"]
    return render_template("cart.html", fruit=fruit)

if __name__ == '__main__':
    app.run(debug=True)


   

