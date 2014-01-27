
from flask import Flask
from flask import render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "SINGalong"
_loggedin = False

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        #checking login stuff
        return redirect(url_for("/AboutUs"));
		
@app.route('/Home', methods = ["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template('Home.html')

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

@app.route('/belly', methods = ["POST", "GET"])
def Belly():
	if request.method == "GET":
		return render_template('belly.html')		

@app.route('/boyshiphop', methods = ["POST", "GET"])
def BoysHH():
	if request.method == "GET":
		return render_template('boyshiphop.html')

@app.route('/Contemporary', methods = ["POST", "GET"])
def Contemp():
	if request.method == "GET":
		return render_template('contemp.html')

@app.route('/girlshiphop', methods = ["POST", "GET"])
def Girlshiphop():
	if request.method == "GET":
		return render_template('girlshiphop.html')		

@app.route('/step', methods = ["POST", "GET"])
def Step():
	if request.method == "GET":
		return render_template('step.html')
		
@app.route('/latin', methods = ["POST", "GET"])
def Latin():
	if request.method == "GET":
		return render_template('latin.html')

@app.route('/rave', methods = ["POST", "GET"])
def Rave():
	if request.method == "GET":
		return render_template('rave.html')


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)
