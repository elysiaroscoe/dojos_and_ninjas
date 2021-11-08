
from flask_app import app
from flask import render_template, redirect, request, session ,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

#view all dojos on main page
@app.route("/dojos")
def read_all():
    all_dojos = Dojo.get_all()
    return render_template("view_dojos.html", all_dojos = all_dojos)

#use main page button to post dojo
@app.route('/dojos/new', methods = ["POST"])
def create():
    Dojo.save(request.form)
    return redirect('/dojos')

#click on dojo in table to see dojo table of ninjas
@app.route('/dojos/<int:id>')
def read_one(id):
    dojo = Dojo.get_one({"id" : id})
    return render_template('one_dojo.html', dojo = dojo)





