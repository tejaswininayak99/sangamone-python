#fun programming with python
'''
12)Find Resolution of an Image

    with open(filename,'rb') as img:
    img_file.seek(163)
    a = img_file.read(2)
    height = (a[0] << 8) + a[1]
    a = img_file.read(2)
    te9(assignment).py

'''
from flask import Flask,render_template,request
image=Flask(__name__)
@image.route("/",methods=["POST","GET"])
def img_res(filename):
  a=request.form.get("input1")
if request.method=="POST":
   
      with open(filename,'rb') as im:
         img_res.seek(163)
         a= img_res.read(2)
         height=(a[0]<<8)+a[1]
         a=img_res.read(2)
         width=(a[0]<<8)+a[1]
return render_template("image.html",message1=width,message2=height)
if __name__=="__main__":
       image.run(debug=True)
img_res=input1("img1.png")

   

