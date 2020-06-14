from PIL import Image, ImageDraw
from pathlib import Path
import re
import os
import photos
 

all_files = os.listdir()
png_files = filter(lambda x: (Path(x).suffix == '.PNG' or Path(x).suffix == '.png') and not ('cropped' in x), all_files)

box_x, box_y = 3,460
box_w, box_h = 1420, 1250

box = [(box_x, box_y), (box_x + box_w, box_y + box_h)]

#for x in ['IMG_0074.PNG']:
for x in png_files:
    print(f"Processing {x}")
    img = Image.open(x)
    #img_draw = ImageDraw.Draw(img)
    #img_draw.rectangle(box, outline='red')

    img_cropped = img.crop((box_x, box_y, box_x+box_w, box_y+box_h))

    img_cropped.show()

    p = re.compile(r'(\w+)(\.\w+)')
    m = p.match(x)
    filename = m.group(1)
    ext = m.group(2)
    new_filename =    'cropped_' + filename + ext
    img_cropped.save(new_filename)
  
  
