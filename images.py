from PIL import Image,ImageFilter
# filtered_image=img.filter(ImageFilter.BLUR) 
# # We can use other function like SMOOTH SHARPEN ETC
# filtered_image.save("blur.png","png")
# We can convert our image to gray let's see how to do that
# converted_img=img.convert("L")
# converted_img.save("grey.png","png")
# converted_img.show()
# crooked=img.rotate(90)
# crooked.save("90Degree.png","png")
# resize=img.resize((300,300))
# resize.save("resized.png","png")
# box=(100,100,400,400)
# cropped_image=img.crop(box)
# cropped_image.save("cropped_image.png","png")
# img=Image.open("./astro.jpg")
# new_image=img.resize((400,400))
# new_image.save("new_image.png","png")
# For keeping the aspect ratio we use Thumbnail
img=Image.open("./astro.jpg")
img.thumbnail((400,200))
img.save("Thumbnail.png","png")
print(img.size)