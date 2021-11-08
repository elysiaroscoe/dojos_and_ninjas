# from types import MethodDescriptorType
# from flask_app import Flask
from flask_app import app
from flask import render_template, redirect, request, session ,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

#create ninjas
@app.route("/ninjas")
def ninja_form():
    return render_template("new_ninja.html", all_dojos = Dojo.get_all())

#use ninjas button to post to database
@app.route('/ninjas/new', methods = ["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
    #i want it to redirect to the dojo that it belongs to
    # f"/dojos/{dojo_id}"
    # f"/dojos/{id}"
    # dojo = Dojo.get_one({"id" : id})