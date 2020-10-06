import PIL
from PIL import Image
import os

for filename in os.listdir('extract_videos'):
    if not filename.startswith('.'):
        for filenameception in os.listdir('extract_videos/' + str(filename)):
            if filenameception.endswith('.jpg'):

                im = Image.open("extract_videos/" + str(filename) + '/' + str(filenameception))

                width, height = im.size

                left = width/10
                top = 0
                right = 4 * width / 5
                bottom= 9 * height / 10

                if im.mode != "RGB":
                    im = im.convert("RGB")

                im1 = im.crop((left, top, right, bottom))
                if not os.path.exists('cropped_frames'):
                    os.makedirs('cropped_frames')
                if not os.path.exists("cropped_frames/" + "cropped" + str(filename)):
                    os.makedirs("cropped_frames/" + "cropped" + str(filename))
            
                im1.save("cropped_frames/" + "cropped" + str(filename) + '/' + str(filenameception))