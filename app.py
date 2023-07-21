from flask import Flask, render_template

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-goes-here'

# Import the views to register the routes
from views import *

if __name__ == '__main__':
    app.run(debug=True)