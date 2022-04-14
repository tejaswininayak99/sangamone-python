from flask import Flask,render_template,request
add2num=Flask(__name__)
@add2num.route("/",methods=["POST","GET"])
def add():
    
    num1=[]
    num2=[]
    if request.method=="POST":
        num1=int(request.form.get("input1"))
        if request.method=="POST":
            num2=int(request.form.get("input2"))
            add=sum(num1+num2)
            return render_template("add.html",message1=add)
if __name__=="__main__":
    add2num.run(debug=True)
            
            
        
            
    
        

    
    




    
   
        
        
        
        
    
        
                            
