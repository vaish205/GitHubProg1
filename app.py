from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/register">Register</a>'

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success', methods=['POST'])
def success():
    return '<h2>Registration Successful</h2>'

app.run(debug=True)