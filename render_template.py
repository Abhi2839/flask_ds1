# # # render template is used to read html
from flask import Flask, render_template,request,redirect,url_for,jsonify
app = Flask(__name__)
@app.route('/success/<score>') # scrore para success var
def success(score):
    return "the person has score:"+score
@app.route('/fail/<score>') # scrore para success var
def fail(score):
    return "the person has failed and has average score: "+score
@app.route("/")
def hello():
   return render_template('index1.html')

@app.route('/form',methods=["GET","POST"])
def form1():
    if request.method=="GET":
        return render_template('forms.html')
    else:
        maths=float(request.form['maths'])
        chem=float(request.form['chem'])
        phy=float(request.form['phy'])
        average=(maths+chem+phy)/3
        res=""
        if average>=50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res,score=average))
        # return render_template('forms.html',score=average)
        
        
        
@app.route("/api",methods=["POST"])
def sum():
    data=request.get_json()
    a_val=dict(data)['a'] # chaneg to dcit data set
    b_val=dict(data)['b'] 
    return jsonify(a_val*b_val)
    
# @app.route("/about",methods=["GET"])
# def xyz():
#     name = "XYZ"
#     return render_template('about.html', name=name)
# @app.route("/bootstrap")
# def bootstrap():
    
#     return render_template('bootstrap.html')
if __name__ == "__main__":
    app.run()