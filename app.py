from flask import Flask
from flask import render_template, session, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
	
	
@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)