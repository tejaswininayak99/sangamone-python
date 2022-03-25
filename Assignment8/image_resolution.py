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

def img_res(filename):

   with open(filename,'rb') as img:
       img.seek(163)
       a= img.read(2)
       height=(a[0]<<8)+a[1]
       a=img.read(2)
       width=(a[0]<<8)+a[1]

   print("Width X Height: ", width,"X",height)

img_res("img1.png")

