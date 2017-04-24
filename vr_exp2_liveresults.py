from flask import Flask, render_template



app = Flask(__name__, static_folder='static', static_path='')


#
@app.route('/')
@app.route('/cliff.html')
def cliff():
    return render_template('cliff.html', title='Virtual Cliff Experiment')


@app.route('/wall.html')
def wall():
    return render_template('wall.html', title='Virtual Wall Avoidance Experiment')


@app.route('/objectexp.html')
def objectexp():
    return render_template('objectexp.html', title='Virtual Object Exploration Experiment')


@app.route('/<string:path>')
def catchall_path(path):
    # return path
    return render_template(path)


if __name__ == '__main__':
    app.run()
