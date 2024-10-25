# import flast module
from flask import Flask, request, render_template

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route('/', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    # Store the user data in a database or file
  return render_template('register.html')
  return render_template('success.html')

if __name__ == '__main__':  
   app.run(port="8080",debug="true")  
