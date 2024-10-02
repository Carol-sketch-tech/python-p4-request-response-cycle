#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g, make_response, redirect, abort


app = Flask(__name__)

@app.route('/reginald-kenneth-dwight')
def index1():
    return redirect('names.com/elton-john')

@app.before_request
def app_path():
    g.path= os.path.abspath(os.getcwd())

@app.route('/<stage_name>')
def get_name(stage_name):
    match = session.query('StageName').filter(StageName.name == stage_name)[0]
    if not match:
        abort(404)
    return make_response(f'<h1>{stage_name} is an existing stage name!</h1>')

@app.route('/')
def index():
    host =request.headers.get('Host') # this access the request objects to get the host header
    appname = current_app.name  # this access the appliction context to get the app name

    response_body= f'''<h1> The host for this page is {host}</h1>
            <h2> The name of this application is {appname}</h2>
            <h3> The path of this application on the users devoce is {g.path}'''\
    
    status_code= 200
    headers= {}

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


