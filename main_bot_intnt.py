from flask import Flask, render_template, request,redirect
from bot_function import *
import random,os,yaml

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ["I am Good, Do you want to create an ORG or SPACE (if org input as ORG and if space input as SPACE) "]

question2 = ['bye','Bye','good bye','Good Bye']

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('new.html')
    if request.method == 'POST':
        userInput = request.form['human']
        if userInput in greetings:
            return render_template('new.html', bot=random_greeting)
	elif userInput in question:
            return render_template('new.html', bot=responses)
	elif userInput == "ORG":
            return render_template('new.html', bot="Please  fill the details in the link provided below and then input create_ORG for creating new ORG")
	elif userInput == "SPACE":
            return render_template('new.html', bot="Please  fill the details in the link provided below and then input create_SPACE for creating new ORG")
        elif userInput[6:] == "_ORG":
            with open("/home/ec2-user/recent_inbuilt_indent/Intent_new/PCF_chatBot/templates/inputdetails.yml", 'r') as st:
                data=yaml.load(st)
                print(data)
                response1=create_org(data['api_key'],data['username'],data['password'],data['orgname'],data['orgrole'])
               # print(reponse1)
            return render_template('new.html', bot=response1)
            
        elif userInput[6:] == "_SPACE":
            with open("/home/ec2-user/recent_inbuilt_indent/Intent_new/templates/PCF_chatBot/inputdetails.yml", 'r') as st1:
                data1 = yaml.load(st1)
                response2=create_space(data1['api_key'],data1['username'],data1['password'],data1['spacename'],data1['spacerole'],data1['orgname'])
               # print(response2)
                return render_template('new.html', bot=response2)	
        elif userInput in question2:
            return render_template('new.html', bot="Bye")	

#ecapp = Flask(__name__)

@app.route('/popup_onclick/', methods=['GET','POST'])
def popup_onclick():

   if request.method == 'GET':
        return render_template('popup_onclick.html')
   if request.method == 'POST':
        api_key= request.values.get('api_key')
        username=request.values.get('username')
        password=request.values.get('password')
        orgname=request.values.get('orgname')
        spacename=request.values.get('spacename')
        orgrole=request.values.get('orgrole')
        spacerole=request.values.get('spacerole')
        print(api_key.encode('ascii', 'ignore'),username.encode('ascii', 'ignore'),password.encode('ascii', 'ignore'),orgname.encode('ascii', 'ignore'),spacename.encode('ascii', 'ignore'),orgrole.encode('ascii', 'ignore'),spacerole.encode('ascii', 'ignore'))
        with open("/home/ec2-user/recent_inbuilt_indent/Intent_new/PCF_chatBot/templates/inputdetails.yml", 'w') as stream:
            da={}
            da['api_key']=api_key.encode('ascii', 'ignore')
            da['username']=username.encode('ascii', 'ignore')
	    da['password']=password.encode('ascii', 'ignore')
	    da['orgname']=orgname.encode('ascii', 'ignore')
	    da['spacename']=spacename.encode('ascii', 'ignore')
	    da['orgrole']=orgrole.encode('ascii', 'ignore')
	    da['spacerole']=spacerole.encode('ascii', 'ignore')
            yaml.dump(da, stream, default_flow_style=False)

        return  render_template('new.html') 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8070, debug=True)
#    secapp.run(host='0.0.0.0', port=7080, debug=True)			
