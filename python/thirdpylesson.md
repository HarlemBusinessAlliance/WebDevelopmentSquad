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
    Allows you to interact with the operating system your program is running on. You can retrieve the paths of important files, delete files, get info on the user the operating system/computer is registered to, etc.

import datetime
    Supplies you with the ability to retrieve the date and time the operating system has, and output that info in different ways.

    Ex. of methods: .ctime
                    .datetime
                    .getmtime()

import date
    A date object represents a date (year, month and day) in an idealized calendar, the current Gregorian calendar indefinitely extended in both directions.

import time
    A time object represents a (local) time of day, independent of any particular day, and subject to adjustment.

import shutil
    Lets you copy and move files/directories easily

    Ex. shutil.copyfile('data.db', 'archive.db')
        shutil.move('/build/executables', 'installdir')

import random
    Allows you to generate random numbers

    Ex. print(random.choice(['apple', 'pear', 'banana']))

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

    import json - The module that supplies you with all of the methods associated with parsing json data

    json.dumps() - Outputs structured data as JavaScript Object Notation. Just make sure to import the json package!

    with open('strings.json') as json_data: <- An illustration of opening a json file and outputting its contents using .load (leave off the s... .loads() is to be used for strings!)
        d = json.load(json_data)
        print(d)

---
References

https://www.pythonforbeginners.com

https://www.dataquest.io/blog/python-api-tutorial/

https://www.codeproject.com/Articles/1160817/Visual-Studio-Code-Connect-to-Twitter-with-Python