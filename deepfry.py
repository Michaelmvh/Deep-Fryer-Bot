from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import requests
from io import BytesIO                                                              

def imageToLink(img):
    if isinstance(img, Image.Image):
        return img
    elif not isinstance(img, str):
        print("not valid type passed")
        return
    # Import Image from passed URL
    try:
        response = requests.get(img)
        img = Image.open(BytesIO(response.content))                                                         
    except:
        print("error parsing link")
        return
    return img

def deepFryImage(img):
    img = imageToLink(img)
    # Saturation
    enhancer = ImageEnhance.Color(img)
    res = enhancer.enhance(2.0)    

    # Sharpen 
    enhancer = ImageEnhance.Sharpness(res)
    res = enhancer.enhance(100) 

    # Contrast
    enhancer = ImageEnhance.Contrast(res)
    res = enhancer.enhance(100)

    # Return Deep Fried Image
    #res.save('result.png')
    return res

def bottomTextImage(img):
    img = imageToLink(img)
    W, H = img.size

    text = "Bottom Text"
    font = ImageFont.truetype(
        font="unicode.impact.ttf",
        size=350,
        encoding='unic')
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text, font=font)

    stroke_color = (0, 0, 0)
    fill_color = (255, 255, 255)

    draw.text(((W-w)/2, int((H-h)*.99)), text, font=font, fill=fill_color, stroke_width=2, stroke_fill=stroke_color)
    return img

def memeImage(img):
    img = imageToLink(img)
    return bottomTextImage(deepFryImage(img))

## Example of calling this function
#memeImage("https://www.salton.com/wp-content/uploads/2016/04/DF1233_2-1.jpg").save('result.png')