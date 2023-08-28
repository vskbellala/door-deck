import pandas as pd
import os
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

txt = pd.read_csv("tags.csv", header=None)
font = ImageFont.truetype("ComicSansMS3.ttf", 30)
font_small = ImageFont.truetype("ComicSansMS3.ttf", 14)

os.makedirs("photos", exist_ok=True)
os.makedirs("tags", exist_ok=True)
os.makedirs("people", exist_ok=True)

os.chdir("photos/")

fill_color = (255,255,255)  # your new background color
image2 = Image.open('tag.jpg')
image2_size = image2.size

lst = os.listdir('.')
ending = '.png'
files = pd.DataFrame(lst)

df_filter = files[files[0].str.lower().str.endswith(ending)]
img_blank = []

for pic in df_filter.values:
    #Read the two images
    image1 = Image.open(pic[0])
    col = pic[0][:-4]
    # print(col)

    im = image1.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
    new_height = image2.width
    new_width = round(new_height*im.width/im.height)
    image1 = im.resize((new_width, new_height),Image.LANCZOS)

    new_image = Image.new('RGB',(image2.width, image1.height+image2.height),(255,255,255))
    new_image.paste(image1,(round(image2.width/2 - image1.width/2),0))
    new_image.paste(image2,(0,round(image1.height)))
    os.chdir("../tags/")
    new_image_name = "{0}_tag.png".format(col)
    new_image.save(new_image_name,"PNG")
    img_blank.append(Image.open(new_image_name))
    os.chdir("../photos/")


os.chdir("../tags/")
lst = os.listdir('.')
ending = '_tag.png'
files = pd.DataFrame(lst)
df_filter = files[files[0].str.lower().str.endswith(ending)]
tag_dis = np.repeat(df_filter.values, len(txt) / len(df_filter.values) + 1)
random.shuffle(tag_dis)

img_final = []

for i in range(len(txt.values)):
    x = txt.values[i]
    t = x[0]
    im3 = tag_dis[i]
    image3 = Image.open(im3)
    print("{0}, {1}".format(t, im3))
    # image3 = Image.open('cyan_tag.png')
    draw = ImageDraw.Draw(image3)
    draw.text((round(image2.width/2),round(image3.height - image2.height/2)), x[1], (0,0,0), font=font, anchor='mm')

    if not(pd.isna(x[2])):
        draw.text((image2.width,0), x[2], (0,0,0), font=font_small, anchor='rt')

    # image3 = image3.resize((300,375))

    os.chdir("../people/")
    image3.save("{0}.png".format(t.replace(' ','_').replace("'","")),"PNG")
    img_final.append(image3)
    os.chdir("../tags/")

os.chdir("..")
img_final+=img_blank
img_final[0].save(
    "deck_all.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=img_final[1:]
)