from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the index page!'

@app.route('/play/<int:number>/<string:color>')
def play(number, color):
    return render_template('index.html', boxes=number, color=color)

@app.errorhandler(404)
def my_error(err_no):
    return f"Sorry! No response.  Try again. ({err_no})"

if __name__=="__main__":
    app.run(debug=True)