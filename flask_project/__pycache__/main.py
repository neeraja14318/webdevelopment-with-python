from flask import Flask,redirect,url_for
app=Flask('__name__')

@app.route("/home")#
def hello():
	return "<h1>hello welcome to bvc college</h1>"
@app.route("/about")
def about():
	return "<h1>about page</h1> "
@app.route("/data/<name>/<regd>/<branch>/<year>/<sem1>/<sem2>")
def data(name, regd,branch,year,sem1,sem2):
	name="Ramya"
	regd="5A7"
	branch="CSE"
	year="2nd"
	sem1="8.90"
	sem2="8.15"
	return """<h1>My name is {}	\n my roll number is{}\nMy branch is {}\n year of study {}\nsem1 result is  {}\nsem2 result is {}</h1>""".format(name,regd,branch,year,sem1,sem2)
@app.route("/admin")
def admin():
		return "<h1>Welcome to admin page</h1>"
@app.route("/student")
def student():
	return "<font color='red'>hello welcome to student page</font>"
@app.route("/faculty")
def faculty():
	return "welcome to faculty data"
@app.route("/user/<name>")
def user(name):
	if(name=="faculty"):
	    return redirect(url_for("faculty"))
	 if(name=="student"):
	 	return redirect(url_for("student"))
	 if(name=="admin"):
	 	return redirect(url_for("admin"))
	 else:
	 	return "The url not found"
if(__name__=='__main__'):
	app.run(debug=True)