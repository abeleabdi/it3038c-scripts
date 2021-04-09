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




