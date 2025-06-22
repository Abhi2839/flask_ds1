from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello world"

# variable rule
# @app.route('/success/<score>') # scrore para success var
# def success(score):
#     return "the person has score:"+score
@app.route('/success/<int:score>') # scrore para success var
def success(score):
    return "the person has score:"+str(score)
@app.route("/Abhey")
def hi():
    return "Hello from abhey"
app.run()