from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify,request





#from flask_cognito_auth import CognitoAuthManager
#from flask_cognito_auth import login_handler
#from flask_cognito_auth import logout_handler
#from flask_cognito_auth import callback_handler
import boto3
import csv
# some bits of text for the page.


# EB looks for an 'application' callable by default.
application = Flask(__name__)

var =5

@application.route('/')
def index():
       return render_template('/Login.html')

       

@application.route('/FrontEnd')
def frontlink():
       return render_template('/FrontEnd.html')

@application.route("/register")
def registerlink():
        return render_template("register.html")

        
@application.route("/Logout")
def logoutlink():
        return render_template("Logout.html")

@application.route("/FrontEnd")
def getnum():
       return render_template("FrontEnd.html",var)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=True)
