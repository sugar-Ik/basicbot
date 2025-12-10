from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Route for the root URL[](http://127.0.0.1:5000/)
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1><p>Welcome to my simple Flask app!</p>'

# Optional: another route
@app.route('/about')
def about():
    return '<h2>About</h2><p>This is a minimal Flask example.</p>'

# Run the app when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
