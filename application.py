from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import jsonify,request,flash
import requests
import json





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

@application.route('/Query',  methods=['POST','GET'])
def scandb():
       show_table = False
       data = ''
       if request.method == 'POST':
              catg = ""
              sub = ""
              st = "" 
              catg = request.form["category"]
              sub = request.form["suburb"]
              st = request.form["state"] 

              if catg == '' and sub == '' and st =='':
                     flash("Enter atleast one field")     
              URL = "https://a5wioxlda4.execute-api.us-east-2.amazonaws.com/test/dynamo"

              header = {"Content-Type": "application/json"}

              payload = get_filter_condition(category=catg,suburb=sub,state=st)
              print(payload)
              r = requests.request("POST", URL, headers=header,data = payload)
              
              data = jsonify(r.text)
             
              return data
              #data = q['Items']
              show_table = True
              
              #if data:
               #      render_template('FrontEnd.html',data=enumerate(data),show_table = show_table)
              #else:
               #      flash('No result is retrieved. Please query again')
              
       #return render_template('FrontEnd.html')
       #return render_template('/dbQuery.html')



def get_filter_condition(category, suburb, state):
    if(category):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val","ExpressionAttributeValues": {":val": {"S": "'+category+'"}},"ExpressionAttributeNames":{"#cat":"category"},"ReturnConsumedCapacity": "TOTAL"}'

    if(suburb):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val","ExpressionAttributeValues": {":val": {"S": "'+suburb+'"}},"ExpressionAttributeNames":{"#cat":"Suburb"},"ReturnConsumedCapacity": "TOTAL"}'

    if (state):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val","ExpressionAttributeValues": {":val": {"S": "'+state+'"}},"ExpressionAttributeNames":{"#cat":"State"},"ReturnConsumedCapacity": "TOTAL"}'

    if(category and suburb):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val AND #su = :val2","ExpressionAttributeValues": {":val": {"S": "'+category+'"},":val2": {"S": "'+suburb+'"}},"ExpressionAttributeNames":{"#cat":"category","#su":"Suburb"},"ReturnConsumedCapacity": "TOTAL"}'


    if(category and state):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val AND #su = :val2","ExpressionAttributeValues": {":val": {"S": "'+category+'"},":val2": {"S": "'+state+'"}},"ExpressionAttributeNames":{"#cat":"category","#su":"state"},"ReturnConsumedCapacity": "TOTAL"}'

    if(suburb and state):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val AND #su = :val2","ExpressionAttributeValues": {":val": {"S": "'+state+'"},":val2": {"S": "'+suburb+'"}},"ExpressionAttributeNames":{"#cat":"State","#su":"Suburb"},"ReturnConsumedCapacity": "TOTAL"}'

    if(suburb and state and category):
        filter_condition = '{"TableName": "doctors_database","FilterExpression": "#cat = :val AND #su = :val2 AND #st = :val3","ExpressionAttributeValues": {":val": {"S": "'+category+'"},":val2": {"S": "'+suburb+'"},":val3": {"S": "'+state+'"}},"ExpressionAttributeNames":{"#cat":"category","#su":"Suburb","#st":"State"},"ReturnConsumedCapacity": "TOTAL"}'

       
    return filter_condition




# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug=True)
