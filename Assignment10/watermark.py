from PIL import Image,ImageDraw,ImageFont
imagee=Image.open('img1.png')
width,height=imagee.size
draw=ImageDraw.Draw(imagee)
text="Great Picture"
font=ImageFont.truetype('arial.ttf',55)
textwidth,textheight = draw.textsize(text,font)
margin=50
x=width-textwidth-margin
y=height-textheight-margin
draw.text((x,y),text,font=font)
imagee.show()

