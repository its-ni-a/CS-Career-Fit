# -- Flask Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

## Additional Imports
import datetime as dt
import model as model

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = dt.datetime.now()

# -- Routes --
@app.route('/')
@app.route('/index')
def index():
    data = {
    }
    return render_template('index.html', data=data)

@app.route('/base')
def base ():
    data = {
        
    }
    return render_template('base.html', data=data)

@app.route('/homepage')
def homepage():
    data = {
        
    }
    return render_template('homepage.html', data=data)

@app.route('/quiz')
def quiz():
    data = {
        
    }
    return render_template('/quiz.html', data=data)

@app.route('/descriptions')
def descriptions():
    data = {
        
    }
    return render_template('descriptions.html', data=data)

@app.route('/resources')
def resources():
    data = {
        
    }
    return render_template('resources.html', data=data)

@app.route('/creative_design', methods=['GET', 'POST'])
def creative_design():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)

@app.route('/advanced_technology', methods=['GET', 'POST'])
def advanced_technology():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)

@app.route('/financial_technology', methods=['GET', 'POST'])
def financial_technology():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)

@app.route('/business_technology', methods=['GET', 'POST'])
def business_technology():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)

@app.route('/cybersecurity_it', methods=['GET', 'POST'])
def cybersecurity_it():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)

@app.route('/tech_related', methods=['GET', 'POST'])
def tech_related():
    if request.method == "GET":
        return render_template('.html')
    else:
        form=request.form
        print (form)
        score = model.calculate_score(form)
        template = model.score_category(score)
        print (score)
        category= model.score_category(score)
        print(category)    
        data = {
            'category': category
        }
        return render_template(template, data=data)