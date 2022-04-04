from flask import Flask,render_template,request
calculatorflask=Flask(__name__)
@calculatorflask.route("/",methods=["POST","GET"])

def add(m,n):
    m+n=output
def sub(m,n):
     m-n=output
def mul(m,n):
     m*n=output
def div(m,n):
     m/n=output
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if request.method=="POST":
        num1=int(request.form.get("input1"))
        num2=int(request.form.get("input2"))
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1,num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    break
else:
    print("input is not valid")
    return render_template("calculator.html",message1=output)
if __name__=="__main__":
    calculator.run(debug=True)
   


