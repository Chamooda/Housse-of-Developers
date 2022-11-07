import hashlib
from PIL import Image
import random

def ImgGenerator(user_count):
    imag = Image.open("bird 2.png","r")
    rgba = imag.convert('RGBA')
    # pix = list(rgba.getdata())


    da_list = []

    # for i in pix:
    #     i = list(i)

    # rgba.putdata(pix)

    for i in range (1032):
        #da_string = str(i[0])+str(i[1])+str(i[2])+str(i[3])+"-"
        da_tuple = []
        for j in range (4):
            da_tuple.append(random.randint(0,255))
        
        da_list.append(tuple(da_tuple))


    rgba.putdata(da_list)
    rgba.save(f'transparent_image.png'+{user_count}, 'PNG')
    #rgba.save(f'transparent_image.png'+{user_count}, 'PNG')

    return (f'transparent_image.png'+{user_count})

    

    # #5d4bc4deda63297907dbb0dceeb8400e6d7fc21aa52bc74778c62999fb807806





