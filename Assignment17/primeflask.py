from flask import Flask,render_template,request
prime=Flask(__name__)
@prime.route("/",methods=["POST","GET"])
def num1():
    num1=[]
    if request.method=="POST":
        num=int(request.form.get("input1"))
        if num>1:
            for i in range(2,num):
                num1=((num % i) == 0)
                return render_template("prime.html",message1=num1)
            else:
                return render_template("prime.html",message2=num1)
                    
            
                
        
if __name__=="__main__":
    prime.run(debug=True)
                    
                        
                    
                
                
                    
                
                    
    
    
    
        
        
                

    
        
            
                
            
        
            
        
                        
           
               
             
            
            
            
                
                
        
          
        
                
                        
                        
             
                 
                     
                     
                   
                     
                    
                    
                        
                    
                        
                    
                        
                    
            
