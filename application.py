from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify
from flask_cognito_auth import CognitoAuthManager
from flask_cognito_auth import login_handler
from flask_cognito_auth import logout_handler
from flask_cognito_auth import callback_handler


# some bits of text for the page.


# EB looks for an 'application' callable by default.
application = Flask(__name__)


application.config['AWS_DEFAULT_REGION'] = 'us-east-1'
application.config['AWS_COGNITO_DOMAIN'] = 'https://mentalhealthdashboard.auth.us-east-1.amazoncognito.com'
application.config['AWS_COGNITO_USER_POOL_ID'] = 'us-east-1_aH1Hu64wq'
application.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = '6racl6f38flj3g55c0ervm770u'
application.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = '16s7vtq9q91h7o6kb1k0lbkjo6ce4er37pk2okatgr1o7d61qqec'
application.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = '16s7vtq9q91h7o6kb1k0lbkjo6ce4er37pk2okatgr1o7d61qqec'
application.config['AWS_COGNITO_REDIRECT_URL'] = 'http://localhost:5000'

aws_auth = AWSCognitoAuthentication(application)


@application.route('/')
def index():
       return render_template('/FrontEnd.html')

@application.route("/register")
def registerlink():
        return render_template("register.html")


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()