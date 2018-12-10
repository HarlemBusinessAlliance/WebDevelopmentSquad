Flies 
Oh. No.
Files
Yup. Files.


##FILES!

Make sure to create your file names with ONLY [az][AZ][09][_] characters, no spaces or dashes or any other special characters


open() - Takes two parameters: The file path/file name, and one of the following mode 

'''
                      | r   r+   w   w+   a   a+
    ------------------|--------------------------
    read              | +   +        +        +
    write             |     +    +   +    +   +
    write after seek  |     +    +   +
    create            |          +   +    +   +
    truncate          |          +   +
    position at start | +   +    +   +
    position at end   |                   +   +
'''

.read() - Retrieve all of the content in a file
.write() - Writes stuff to an opened file
.mode - Is it readable? Writeable? Appendable
If you want to read all the lines of a file in a list you can also use list(), readline(), or readlines() for retrieving more than one line.
.close()

Btw you can chain methods together in programming languages. For example"
'''
    data = open('a.zip', 'rb').read()
'''

Moving and copying files can be done with the module shutil

When you retrieve the innards of a file you can process the text with string operations

---
## Some commonly used modules
import requests
    Used to connecto to APIs
    Use pip or easy_install to install the requests module in the terminal ("pip install requests" for Windows)
import os
import datetime
    .ctime
    .datetime
    .getmtime()
import time
import shutil
    shutil.copyfile('data.db', 'archive.db')
    shutil.move('/build/executables', 'installdir')

'''
    import random
    print(random.choice(['apple', 'pear', 'banana']))
'''


---
## Web data. Yummee.

Gimme the outside data
'''
    import requests

    url = 'https://url'
    data = '{  "platform": {    
        "login": {      "userName": "name",      "password": "pwd"    }  } 
    }'

    response = requests.post(url, data=data, headers={"Content-Type": "application/json"})

    print(response)

    sid=response.json()['platform']['login']['sessionId']   # gimme data!

    print(response.text)
    print(sid)
'''

---
## JSON

import json 

json.dumps() - Outputs structured data as JavaScript Object Notation. Just make sure to import the json package!

---
## Parsing in HTML

'''
    import HTMLParser
#or
    from HTMLParser import HTMLParser

    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print "Encountered a start tag:", tag

        def handle_endtag(self, tag):   
            print "Encountered an end tag :", tag

        def handle_data(self, data):
            print "Encountered some data  :", data

    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1></body></html>')
'''

---
References

https://www.dataquest.io/blog/python-api-tutorial/

https://www.codeproject.com/Articles/1160817/Visual-Studio-Code-Connect-to-Twitter-with-Python