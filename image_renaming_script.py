'''Author Okeng Fernando --------> okengfernando@gmail.com 
   Ver: Python 3.x'''

# Python program to rename all collated images to a desired format


import os
import sys
import time

import progress_bar_helper

def main():

    FOLDER_PATH = "/mnt/7680BDCD80BD9459/UPWK/PAR/SOURCING_TASKS/sourcing_RFI003/raw_images"  #insert path to your raw images
    FILE_NAME = 'RFI0003-raw-image_0' #Insert your Desired Filename

    global COUNT 
    COUNT = 1   #insert desired output format NB: avoid / because it throws a FILE-NOT-FOUND Error

    if FOLDER_PATH == '' or FILE_NAME == '' or FOLDER_PATH == ' ' or FILE_NAME == ' ':
        sys.exit("PATH or FILE_NAME cant be left EMPTY!!")

    for i in FILE_NAME:
        if "/" == i:
            sys.exit("Error !!, remove foward or Back slash from FILE_NAME")

    os.chdir(FOLDER_PATH)   
    print(os.getcwd())      #displays current working directory
    
     #This variable is what is a  trailing figure that is attached to the file_name
    
    # Function to increment count 
    # to make the files sorted.
    def increment():
        global COUNT
        COUNT = COUNT + 1
    

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f) 
        f_name = FILE_NAME + str(COUNT)  
        increment()
        
        new_name = '{}{}'.format(f_name, f_ext)
        os.rename(f, new_name)
        #time.sleep(0.05)
        progress_bar_helper.progressBar(COUNT, len(os.listdir()),'renaming')
        
    print("successfully renamed {} files".format(len(os.listdir())))

def log_start():
    print("--------------------------------- Starting Script -------------------------------------")
    print("\n")

def log_done():
    print("\n")
    print("************************************** Done! *************************************** ")


#Driver code to start script
if __name__ == "__main__":
    log_start() #This log helps us show script is running
    main()
    log_done() #This log helps us check if the script is done and complete
