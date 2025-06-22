from flask import Flask,request,render_template,url_for

app=Flask(__name__)
@app.route("/",methods=["POST","GET"])

def calculator():
    result=" "
    if request.method=="POST":
        try:
            num1=float(request.form["num1"])
            num2=float(request.form["num2"])
            operation=request.form["operation"]
            if operation=="add":
                result=num1+num2
            elif operation=="sub":
                result=num1-num2
            elif operation=="multi":
                result =num1*num2
            elif operation=="div":
                try:
                    result= num1/num2
                except ZeroDivisionError:
                    result="Division by zero is not defined"
                    # return 0
                # return num1/num2
                
            else:
                result="Invalid operation"
        except Exception as e:
            result=f"Error: {e}"
    return render_template("calc.html",result=result)
                
          
app.run()