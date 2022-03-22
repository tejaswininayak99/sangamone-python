from flask import Flask,render_template,request
factorial2=Flask(__name__)
def print_table(num): 
    
    for i in range(1,11): 
        #print(num,' x ', i, ' = ',num*i)
       
        output=num*i

        n = int(input("Please Enter a number to print its multiplication table:"))

    return render_template("multiplication.html",message1=output)
if __name__=="__main__":
    factorial2.run(debug=True)
