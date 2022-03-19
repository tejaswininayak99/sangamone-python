from flask import Flask,render_template
PALINDROMEflask=Flask(__name__)
@PALINDROMEflask.route("/",methods=["POST","GET"])
def diamond():
    
    str=input(("Enter a string"))
    if(str==str[::-1]):
                  print("The string is a palindrome")
    else:
               print("Not a palindrome")
    return render_template("palindrome.html")
if __name__=="__main__":
        PALINDROMEflask.run(debug=True)
        
            
