import os
from random import randint
from flask import Flask, render_template, url_for, request, json, app


@app.route('/')
@app.route('/main_page')
def home_page():
    return render_template('home_page.html', title='Домашняя страница')

app = Flask(__name__)
@app.route('/member')
def member():
    with open('templates/members.json', 'r', encoding='utf') as f:
        data = json.loads(f.read())
        data = data['members'][randint(0, 3)]
    return render_template('members.html', data=data)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')