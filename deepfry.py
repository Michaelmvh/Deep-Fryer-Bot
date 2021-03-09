from PIL import Image, ImageEnhance  
import requests
from io import BytesIO                                                              

def deepFryImage(imageURL):
    # Import Image from passed URL
    try:
        response = requests.get(imageURL)
        img = Image.open(BytesIO(response.content))                                                                 
    except:
        print("error parsing link")
        return

    # Saturation
    enhancer = ImageEnhance.Color(img)
    res = enhancer.enhance(2.0)    

    # Sharpen 
    enhancer = ImageEnhance.Sharpness(img)
    res = enhancer.enhance(100) 

    # Contrast
    enhancer = ImageEnhance.Contrast(res)
    res = enhancer.enhance(100)

    # Return Deep Fried Image
    #res.save('result.png')
    return res

## Example of calling this function
#deepfry("https://www.salton.com/wp-content/uploads/2016/04/DF1233_2-1.jpg")