from PIL import Image
import os
curr = Image.open(r"C:\Users\lokes\Downloads\car1.jpg")
pixel = curr.load()
brightness_level= 1
bright_img = Image.new("RGB", curr.size)
for i in range(curr.width):
    for j in range(curr.height):
        r, g, b = pixel[i,j]
        r = min(255, int(r*brightness_level))
        g = min(255, int(g*brightness_level))
        b = min(255, int(b*brightness_level))
        bright_img.putpixel((i,j), (r,g,b))
bright_img.save("new_image.jpg")
print("Brightened image saved successfully..")
