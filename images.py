from PIL import Image, ImageFilter

img=Image.open('./pikachu.jpg')
#filtered_img=img.filter(ImageFilter.BLUR)
#filtered_img=img.filter(ImageFilter.SMOOTH)
#filtered_img=img.filter(ImageFilter.SHARPEN)
filtered_img=img.convert('L')

# print(img)      # use powershell and run 'python images.py'
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

#filtered_img.save("blur.png", 'png')
#filtered_img.save("smooth.png", 'png')
#filtered_img.save("sharpen.png", 'png')
filtered_img.save('grey.png','png')