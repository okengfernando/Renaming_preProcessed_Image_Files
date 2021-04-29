'''Author Okeng Fernando --------> okengfernando@gmail.com 
   Ver: Python 3.x'''

# Python program to rename all collated images
# Into the Desired  

import os
  
os.chdir('/home/fernando/raw_script_processor/collated/collated_IR_images')   #insert path to your raw images
print(os.getcwd())      #displays current working directory
COUNT = 1
  
# Function to increment count 
# to make the files sorted.
def increment():
    global COUNT
    COUNT = COUNT + 1
  

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_name = "RFI007_PAR09_ Vertical, 1m GSD_Wildfire_EO-IR_0" + str(COUNT)  #insert desired output format eg RFI006_PAR08_Vertical, 1m GSD_SAR-Aviation_0
    increment()
    
    new_name = '{} {}'.format(f_name, f_ext)
    os.rename(f, new_name)