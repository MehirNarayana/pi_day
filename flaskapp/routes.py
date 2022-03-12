from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_wtf import FlaskForm
from flaskapp.forms import NumberForm
from flaskapp import app
from flaskapp.pi import Solution
#from flaskapp.scraping_script import Script
'''import re
import json'''


@app.route("/", methods=["POST", "GET"])
def index():



    form = NumberForm()


    if request.method == "POST":

        get_data = request.form['number']

        #try:
        number = int(get_data)
        obj = Solution()
        obj.solve(number)
        get = str(obj.return_solution())

        #except:
         #   return render_template('index.html', templates='templates', form=form, number_result='You either entered a character that is not a number and/or entered a number that is not in between the range of 0-250', name='', date='')

        return render_template('index.html', templates='templates', form=form, number_result=get)
    
    else:
        return render_template('index.html', templates='templates', form=form, number_result='')