## Flask app routing
from flask import Flask, render_template, request, redirect, url_for, jsonify

## create a simple flask application.
## flask application will be denaote by app.
## __name__ is the entry point of the program.
app=Flask(__name__)

## methods: GET(default), POST
@app.route("/",methods=['GET'])
def welcome():
    return "<h1>Welcome to the Home Page</h1>"

@app.route("/index",methods=['GET'])
def index():
    return "<h2>Welcome to the Index Page</h2>"

## If we want to give any parameters in our URL then it is called variable rule.
@app.route("/success/<int:score>")
def success(score):
    return "person passed and the score is: "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "person filed and the score is: "+ str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        history=float(request.form["history"])

        average_marks=(maths+science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))
        #return render_template("form.html",score=average_marks)

@app.route("/api", methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)

## if we don't give debug=True the  every time we made some changes in our code we have to stop our server.
## by default app.run() will have 2 parameters: 1) URL 2) port
if __name__=="__main__":
    app.run(debug=True)

