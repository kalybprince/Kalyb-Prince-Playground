from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return 'Welcome to the index page!'  # Return the string 'Hello World!' as a response

@app.route('/play/<int:number>/<string:color>')
def play(number, color):
    return render_template('index.html', boxes=number, color=color)

@app.errorhandler(404)
def my_error(err_no):
    return f"Sorry! No response.  Try again. ({err_no})"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.