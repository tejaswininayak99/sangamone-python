from flask import Flask,render_template,request
PALINDROMEflask=Flask(__name__)
@PALINDROMEflask.route("/",methods=["POST","GET"])
def palin():
    pal=[]
    if request.method=="POST":
        pal=str(request.form.get("input1"))
    if(pal==pal[::-1]):    
        return render_template("palindrome.html",message1=pal)
    else:
        return render_template("palindrome.html",message2=pal)

if __name__=="__main__":
        PALINDROMEflask.run(debug=True)
        
            
