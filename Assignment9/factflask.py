from flask import Flask,render_template,request
factorial=Flask(__name__)
@factorial.route("/",methods=["POST","GET"])
def fact2():
    fact2=1
    if request.method=="POST":
        num1=int(request.form.get("input1"))
        for i in range(1,num1+1):
            fact2=fact2*i
    return render_template("factorial.html",message1=fact2)
if __name__=="__main__":
    factorial.run(debug=True)
    
