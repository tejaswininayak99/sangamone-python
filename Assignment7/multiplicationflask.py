from flask import Flask,render_template,request
multiplicationflask=Flask(__name__)
@multiplicationflask.route("/",methods=["GET", "POST"])
def table():
    num=1
    
    if request.method=="POST":
        num=int(request.form.get("input1"))
    for i in range(1,11): 
        input1=(num,' x ', i, ' = ',num*i)
        
        return render_template("multiplication.html",message1=table(input1))
        #return render_template("multiplication.html",message1=input1)
        #return render_template("multiplication.html")
    #table(input1)
    
if __name__=="__main__":
    multiplicationflask.run(debug=True)

