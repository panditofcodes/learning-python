from flask import Flask, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)


# Define a route
@app.route("/")
def hello():
    return """
            <h1 style= "text-align:center">Welcome To Flask App</h1>
            <a href="http://127.0.0.1:5000/contact">contact</a>
        """


@app.route("/contact")
def contact():
    return 'Please contact! <a href="https://www.panditofcodes.com" target = "blank">Podes</a>'


@app.route("/login/<username>")
def login(username):
    return redirect(url_for("profile", name=username))


@app.route("/profile/<name>")
def profile(name):
    return f"Profile: {name.capitalize()}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"This is post #{post_id}"


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
