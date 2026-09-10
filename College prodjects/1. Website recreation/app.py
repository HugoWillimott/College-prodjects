#import 'Flask' class
#render template makes it so it acsesses the html files
from flask import Flask, render_template

#creates an instance of 'Flask'
app = Flask(__name__)

#Defining the URL should trigger the function and runs when somone visits said URL and displys what the user sees on the page
@app.route('/')
def Home():
    return render_template('Website.html')

#starts the web server
if __name__ == '__main__':
    app.run(debug=True)