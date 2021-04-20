My App
======
# This is my App

````javascript
Javascript code block to highlight what is happing in my code right now.

```Visual Studio Code edit!


###This is Github Edit!!!
def calculate(a, b, c):
    """Calculate curve value .

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]

    Returns:
        [type]: [description]
    """
    d = 100 * c - 10 * b + c
    return d

def create_app():
    """Create a Flask app .

    Returns:
        [type]: [description]
    """
    @app.route("/")
    def index():
        return jsonify(hello="world")

def sina_xml_to_url_(xml_data):
    """Convert a string of XML to a list of URLs .

    Args:
        xml_data ([type]): [description]

    Returns:
        [type]: [description]
    """
    rawurl = []
    dom = parseString(xml_data)
    for node in dom.getElementsByTagName('durl'):
        url = node.getElementsByTagName('url')[0]
        rawurl.append(url.childNodes[0].data)
    return rawurl
 
Usage is very simple. 

First - Run the container for the model inference server

    If you have GPU machine : docker run -it -d --gpus 0 -p 5000:5000 graykode/ai-docstring, after installing nvidia-docker.
    If you have only CPU : docker run -it -d -p 5000:5000 graykode/ai-docstring

Second - Install extension in vscode and use

Cursor must be on the line directly below the definition to generate full auto-populated docstring

    Press enter after opening docstring with triple quotes (""" or ''')
    Keyboard shortcut: ctrl+shift+2 or cmd+shift+2 for mac
        Can be changed in Preferences -> Keyboard Shortcuts -> extension.generateDocstring
    Command: Generate Docstring
    Right click menu: Generate Docstring
    

Features
-AI Quickly generate a docstring snippet that can be tabbed through.
-Choose between several different types of docstring formats.
-Infers parameter types through pep484 type hints, default values, and var names.
-Support for args, kwargs, decorators, errors, and parameter types

Project 2: Phone Tracker by Python

Script:

import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))


from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

Usage: This Python script will track phone any cuntry in the world and the phone carrier. 

Documentation:

-Track Phone Number Location Using Python

-Create a folder with two python files and name them how you want to.

-Install a package using the command: (“pip install phonenumber”).

-On the first python file import the package phonenumber.

-On the second file we will enter our phone number we want to track with the country code: (number = “+1----------”).

-Back on the first file import the phone number and create a variable for the phonenumber country.

-Print description for the number which is English “en”.

-Then from the phonenumber import the carrier.

-Lastly print carrier name for phonenumber service number to emglish.



Project 2: Job Tracker / Job Board Scraper to Email. 

Run: "python job_tracker.py"

Step: I Set up the email

Documentation:

1. We import the build-in libraries then we create one function that takes the message as argument.
2. Then we need to set up the port server with whatever email type and the emails and password.
3. If you use two-factor authentication then you need different password, so go to "myaccount.google.com/security" and creat an app password.
4. Lastly we can set up a connection and then try to log in and send the mail.

Script: I

import smtplib, ssl

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "abeleabdi@gmail.com"
    receiver_email = "abeleabdi@gmail.com"
    password = "jhwq gwvh orxq ypix"
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")

Step II: Job Board Scraper

Documentation:

1. First "Pip install requests" pip install requests the module we need and go to "https://remoteok.io/api" copy the link.
2. Import requests and json, then specify the URL we took from "https://remoteok.io/api" and the keys we wnat to inspect, then we specify the text that we're interested in. For example, Python, javaScript, Backed, ....
3. Creat function and end a get request to the url and get the json data.
4. Inerate over all the results and take onlu the specified keys then we get the tags from the tags key.
5. Convert the list to a set and then call the set.intersection method and if this is true means that at least one if the wanted texts is in the text of the job and we therefore append it to the jobs list.
6. Then return this list from the function then we say d under name equals main and use this function and if we found suitable chops we create a message and send this message with our send email function. 

Script: II

import requests
import json
from send_email import send_email

URL = "https://remoteok.io/api"
keys = ['date', 'company', 'position', 'tags', 'location', 'url']

wanted_tags = ["python"] # remote, javascript, backend, mobile, ...

def get_jobs():
    resp = requests.get(URL)
    job_results = resp.json()
    
    jobs = []
    for job_res in job_results:
        # take only the specified keys
        job = {k: v for k, v in job_res.items() if k in keys}
    
        if job:
            tags = job.get('tags')
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted_tags):
                jobs.append(job)
    
    return jobs

 
if __name__ == '__main__':
    python_jobs = get_jobs()
    
    if python_jobs:
        message = "Subject: Remote Python Jobs!\n\n"
        message += "Found some cool Python jobs!\n\n"
        
        for job in python_jobs:
            message += f"{json.dumps(job)}\n\n"

        send_email(message)
  



