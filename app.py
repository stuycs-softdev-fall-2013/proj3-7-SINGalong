
from flask import Flask
from flask import render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "SINGalong"
_loggedin = False

@app.route('/login',methods=["POST","GET"])
@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        #checking login stuff
        return redirect(url_for("/AboutUs"));

@app.route('/AboutUs', methods = ["POST", "GET"])
def AboutUs():
    if request.method == "GET":
        return render_template('AboutUs.html')

@app.route('/Contact', methods = ["POST", "GET"])
def Contact():
	if request.method == "GET":
		return render_template('Contact.html')

@app.route('/Rules', methods = ["POST", "GET"])
def Rules():
	if request.method == "GET":
		return render_template('Rules.html')

@app.route('/Calendar', methods = ["POST", "GET"])
def Calendar():
	if request.method == "GET":
		return render_template('Calendar.html')

@app.route('/Contemporary', methods = ["POST", "GET"])
def Contemporary():
	if request.method == "GET":
		return render_template('contemp.html')

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
