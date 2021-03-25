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
        encoding='unic')
    draw = ImageDraw.Draw(img)

    stroke_color = (0, 0, 0)
    fill_color = (255, 255, 255)

    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.90

    font = ImageFont.truetype("unicode.impact.ttf", fontsize)
    while font.getsize(text)[0] < img_fraction*W:
        # iterate until the text size is just larger than the criteria
        fontsize += 10
        font = ImageFont.truetype("unicode.impact.ttf", fontsize)

    draw.text((W*.025, (H-fontsize)*1.05), text, font=font, fill=fill_color, stroke_width=2, stroke_fill=stroke_color)
    return img

def memeImage(img):
    img = imageToLink(img)
    return bottomTextImage(deepFryImage(img))

## Example of calling this function
memeImage("https://cdn.discordapp.com/attachments/589552727399464960/824723149097795624/ExRXmrbXMAIQ6Nm.jpg").save('result.png')