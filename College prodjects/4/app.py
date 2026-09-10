#import 'Flask' class
#render template makes it so it acsesses the html files
from flask import Flask, render_template

#creates an instance of 'Flask'
app = Flask(__name__)

#Defining the URL should trigger the function and runs when somone visits said URL and displys what the user sees on the page
@app.route('/<name>')
def Home(name):
    return render_template('home.html', user = name)

@app.route('/about')
def About():
    return render_template('about_us.html')

@app.route('/contact')
def Contact():
    return render_template('contact_us.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ_page.html')

#starts the web server
if __name__ == '__main__':
    app.run(debug=True)