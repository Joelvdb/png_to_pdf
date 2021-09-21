from PIL import Image
import glob

im_list=[]
str_im_list=glob.glob("img/*.png")

for image in str_im_list:
    img=Image.open(image)
    rgb_image = img.convert('RGB')
    im_list.append(rgb_image)

pdf1_filename = "pdf1.pdf"

im_list[0].save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list[1:len(im_list)])
