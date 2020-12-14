########################### Home work
import os
from PIL import Image
import cv2

os.getcwd()
#folder with images to be processed 

raw_folder = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2a-image\\raw"
processed_folder = "C:\\Users\\Zhenya\\Desktop\\PhD MPI NL\\Courses\\Python IMPRS\\session2a-image\\processed"


#end = (480, 360)
#size = (480, 360, 480, 360)
# img_path = os.path.join(raw_folder, "bird.jpg")
# img = Image.open(img_path)
# img_open = Image.open(img_path)
# width = img.width 
# height = img.height

# # defining picture orientation
# if width > height:
#     #img = "landscape"
#     print("landscape")
# else:
#     print("portrait") 

basewidth = 480
baseheight = 360
dim = (basewidth,baseheight)



img_path = os.path.join(raw_folder, "clock.jpg")
img = Image.open(img_path)
img_open = Image.open(img_path)
width = img.width 
height = img.height
print(width)
print(height)
#origin = img.size()
#print(origin)

# defining picture orientation
if width > height:
    #img = "landscape"
    print("landscape -> this is the right ratio.")
else:
    print("portrait -> crop the picture to the landscape ratio (4:3).") 
    print(width, height)

if img.format == "JPEG":
    print("JPG is the right format")
else:
    print("You need to convert the image to JPG")

# # crop image to 4:3 ration
# crop_size = (0,0,480,360)
# img_crop = img.crop(crop_size)
# img_crop.show()


img_cv2 = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
resized = cv2.resize(img_cv2, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized image", resized)
cv2.waitKey(0)
print(resized.shape)
img_resize.save(os.path.join(processed_folder, "clock_p.jpg"))

# #new size
# new_size = (200, 200)
# img_rsz = resized.resize(new_size)
# img_rsz.save(os.path.join(processed_folder, "clock_p.jpg"))
#img_rsz.show()

#img_crop = width/2
#img_crop.save(os.path.join(processed_folder, "bird_c.jpg"))
#img.show()
#image_open = img.open(img_path)
#img.save(os.path.join(processed_folder, "bird_p.jpg"))







# for img new_img_list:
#     image_path = os.path.join(folder with processed pictures, img)
#     image_open = image.open(image_path)
#     width = image_open.width
#     height = image_open.height
#     center = (width/2, height/2)
#     if width > height:
#         landscape = img
#         else:
#             portrait = img
            