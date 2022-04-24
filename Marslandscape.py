from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/landscape')
def carousel():
    return render_template('MarsLandscape.html', title='landscape')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')