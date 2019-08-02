from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base
engine =create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)
session=DBSession()

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
		return render_template("sample.html")
@app.route("/student")
def student():
	return "<font color='blue'>hello welcome to student page</font>"
@app.route("/faculty")
def faculty():
	return "welcome to faculty data"
@app.route("/person/<uname>/<roll>/<dept>")
def person(uname,roll,dept):
	return render_template("sample2.html",name=uname,regd=roll,branch=dept)
@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html",n=num)
@app.route("/user/<name>")
def user(name):
	if(name=="faculty"):
	    return redirect(url_for("faculty"))
	elif(name=="student"):
	 	return redirect(url_for("student"))
	elif(name=="admin"):
	 	return redirect(url_for("admin"))
	else:
	 	return "The url not found"
dummy_data=[
{'name':'Ramya',
'org':'BVC',
'DOB':'26/02/2001'},
{'name':'Bhargavi',
'org':'vsm',
'DOB':'07/10/2000'}]
@app.route("/show")
def data_show():
	return render_template("data_show.html",d=dummy_data)
@app.route("/register")
def reg():
	return render_template("register.html")





@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template("show.html",register=register)




@app.route("/add",methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(
			name=request.form['name'],
			surname=request.form['surname'],
			rollno=request.form['rollno'],
			mobile=request.form['mobile'],
			branch=request.form['branch'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('new.html')

@app.route("/<int:register_id>/edit",methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.rollno=request.form['rollno']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch'] 

		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editedData)


@app.route('/<int:register_id>delete',methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()

	if request.method=="POST":
		session.delete(deletedData)
		return redirect(url_for('showData',register_id=register_id))

	else:
		return render_template('delete.html',register=deletedData)


@app.route("/file")
def upload():
	return render_template("file_upload.html")
















if(__name__=='__main__'):
	app.run(debug=True)