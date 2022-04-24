from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/results/<string:nickname>/<int:stage>/<string:number>')
def results(nickname, stage, number):
    return render_template('sorting.html', title='Results', nickname=nickname, stage=stage, number=number)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')