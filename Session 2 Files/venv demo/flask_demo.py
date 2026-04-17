# Flask is a third-party import. It is not part of the standard library
from flask import Flask, render_template

# The below code is being used for an example. It's fine if it doesn't make sense
app = Flask(__name__)

fruits = ['apple', 'banana', 'coconut']

@app.route('/')
def index():
    return render_template('index.html', fruits=fruits)

app.run(port=5000)

# If you run this code deactivated, it will fail to recognize flask