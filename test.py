from flask import Flask, render_template

app = Flask(__name__)
if __name__ == "__main__":
    app.debug=True
    app.run('0.0.0.0')

@app.route("/index")
def index():
    render_template('test.html')
