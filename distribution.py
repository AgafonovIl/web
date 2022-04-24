from flask import Flask, url_for, request, render_template, json

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    list_of_passangers = ['Ридли Скотт', 'Гарри Поттер', 'Александр Петров']
    return render_template('distribution.html', list_of_passangers=list_of_passangers)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')