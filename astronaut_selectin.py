from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def homepage():
    return render_template('homepage.html', title='Домашняя страница')


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['firstname'])
        print(request.form['lastname'])
        print(request.form['education'])
        print(request.form['file'])
        print(request.form.getlist('add[]'))
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')