import os

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/main_page')
def home_page():
    return render_template('home_page.html', title='Домашняя страница')


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        dirname = r'Web5\static\img'
        files = os.listdir(dirname)
        return render_template('carousel.html', title='carousel', files=files)
    elif request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(r'Web5\static\img', f.filename))
        return "Вернитесь на страницу"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
