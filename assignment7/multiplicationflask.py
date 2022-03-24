from flask import Flask,render_template,request
multiplicationflask=Flask(__name__)
@multiplicationflask.route("/",methods=["GET", "POST"])
def print_table(num): 
    
    for i in range(1,11): 
        print((num,' x ', i, ' = ',num*i))

        n = int(input("Please Enter a number to print its multiplication table:"))
    print_table(n)
    return render_template("multiplication.html",message1=output)
if __name__=="__main__":
    multiplicationflask.run(debug=True)
