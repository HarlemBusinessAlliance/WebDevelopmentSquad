These two exercises were swiped from [the official Flask tutorial repo found here](https://github.com/pallets/flask), where the files are found in their examples folder. Please review the full tutorial if you have any additional questions.

We will recreate the two example apps and make a third, changing the Flaskr blog app into a User Survey app.

Have fun!

---
Install and update using pip:
'''
    pip install -U Flask
'''

A Simple Example
'''
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, Cohort!'
'''

You should see something like the following in the terminal:
'''
    $ env FLASK_APP=test.py # If this didn't work try export FLASK_APP=test.py
    $ flask run
        * Serving Flask app "test"
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
'''