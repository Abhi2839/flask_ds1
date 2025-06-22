
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/index.html",methods=["POST","GET"])
def bmi_calc():
    bmi_index=""
    result=""
    res=""
    todo=""
    bmi_class = ""
    if request.method=="POST":
        try:
            weight=float(request.form['Weight'])
            height=float(request.form['Height'])
        
            bmi_index=round(weight/(height**2),2)
            if bmi_index<18.5:
                result="You are UnderWeight"
                res="1"
                bmi_class = "underweight"
            elif 24.9>=bmi_index>=18.5:
                result="You are healthy person"
                res="2"
                bmi_class = "normal"
            elif 29.9>=bmi_index>=25.0:
                result="You are OverWeight make sure to descrease oil and milk based product.Do Excersie only daily basis."
                res="3"
                bmi_class = "overweight"
            elif bmi_index>30:
                result="Obese,Need to work on health to stay healthy." 
                res="4" 
                bmi_class = "obese"
        except ValueError:
            result="Invalid input.Please enter numeric values only in proper units."
        if res=="1":
            todo="Eat rich in protein diet"
        elif res=="2":
            todo="Maintain the diet and do excerise"
        elif res=="3":
            todo="Start cardio workouts"
        elif res=="4":
            todo=" Recommend consulting a doctor"
            
    return render_template('bmi.html',calc_index=bmi_index,result=result,do=todo,bmi_class=bmi_class)
app.run()