from flask import Flask
import random
app=Flask(__name__)


@app.route('/')
def home():
    return '''<!doctype html>
    <html>
        <body>
            <h1>'good morning '</h1>
            <p style='strong' '30fx'> "good weather"</p>
            <div style= 'background:yellow'> 
                <p style='font-size:500fx ; color:red'>"it's rainning"</p>
            </div>
        </body>
    </html>
    '''



@app.route('/index')
def index():
    return 'random: <strong>'+str(random.random())+'</strong>'


@app.route('/aaa/<id>/')
def read(id):
    return 'random: <strong>'+str(random.random())+id+'</strong>'






app.run(port=5001)

