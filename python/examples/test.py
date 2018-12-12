from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    theHTML = "<h1>Hello Cohort!</h1><p>It's great to see you</p><a href='/lesson'>Next page</a>"
    return theHTML

@app.route('/lesson')
def lesson():
    someText = "Getting familiar with different routes"
    someCalc = 1 + 1
    moreHTML = "<h1>Today's Lesson:</h1><p>" + someText + "</p><p>Btw this site has" + someCalc +"pages!</p><a href='/'>Back to Home</a>"
    return moreHTML