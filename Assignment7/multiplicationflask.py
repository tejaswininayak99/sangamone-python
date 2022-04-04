from flask import Flask,render_template,request
multiplicationflask=Flask(__name__)
@multiplicationflask.route("/",methods=["GET", "POST"])
def table():
    num=1
    num1=1
    if request.method=="POST":
        num1=int(request.form.get("input1"))
    for i in range(1,11): 
        num=i*num1
    
        return render_template("multiplication.html",message1=num)
if __name__=="__main__":
    multiplicationflask.run(debug=True)

