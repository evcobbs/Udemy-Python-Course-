import os
import sys
from PIL import Image

#1. use sys first and second argument 1. file to take from 2. new file for pngs
#typed into command line like .\jpgTOpng.py Pokedex\ new\
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if args work
#print(image_folder, output_folder)

#chek is new/ exist, if not, create
if not os.path.exist(output_folder):
    os.makedirs(output_folder)

#loop through pokedex
#convert to png
#save to new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done!')
