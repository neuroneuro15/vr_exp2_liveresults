from flask import Flask, render_template



app = Flask(__name__, static_folder='static', static_path='')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path>')
def catchall_path(path):
    return render_template(path)


if __name__ == '__main__':
    app.run()
