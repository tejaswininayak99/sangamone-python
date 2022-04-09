from flask import Flask, render_template, request  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
     return render_template('example1.html')  
 
 
  
@app.route('/hello', methods=['POST'])  
def hello():  
    first_name = request.form['first_name']  
    last_name = request.form['last_name']  
    data=' %s %s ' % (first_name, last_name)  
    return render_template('ex1.html',value=data)  
     
  
  
if __name__ == '__main__':  
    #app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)  
    app.run('localhost', 4459) 
