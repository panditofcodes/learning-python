from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return "Hello, World!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
