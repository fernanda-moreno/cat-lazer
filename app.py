from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/up")
def up():
    return render_template('index.html')

@app.route("/right")
def right():
    return render_template('index.html')

@app.route("/left")
def left():
    return render_template('index.html')

@app.route("/down")
def down():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)