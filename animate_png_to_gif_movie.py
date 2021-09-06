#taken from https://pythonprogramming.altervista.org/png-to-gif/
# makes gif from all .png files in the current folder

from PIL import Image
import glob


# Create the frames
frames = []


# path to folder with png images
path= r"C:\Users\Sanna\Documents\Beamtime\NanoMAX_May2020\Analysis\scans429_503\3drecons\recons_ePIE\20210810_1150\temp1"
imgs = glob.glob(path + "\\*.png")

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# does no save in order if frames are numberer 1 2 3 ...11 12
#it does, 1, 11, 12 ... 19, 2, 20, 21 osv
# SOLUTION
# name files  1-9 to end with 01, 02, 03 osv

# Save into a GIF file that loops forever
savepath = path + "\\png_to_gif2.gif"
frames[0].save(savepath, format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=500, loop=1)

print('Animation saved to ')
print(savepath)
