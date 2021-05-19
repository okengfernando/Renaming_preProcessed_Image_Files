'''Author Okeng Fernando --------> okengfernando@gmail.com 
   Ver: Python 3.x'''

# Python program to rename all collated images
# Into the Desired  

import os
import sys

def main():

    FOLDER_PATH = '/mnt/7680BDCD80BD9459/PAR client/sourcing_task RFI009_PAR-0d_Vertical 1m GSD_Bow River South/new collated'  #insert path to your raw images
    FILE_NAME = "RFI009_PAR-0d_Vertical 1m GSD_Bow River South_0"   #insert desired output format NB: avoid / because it throws a FILE-NOT-FOUND Error

    for i in FILE_NAME:
        if "/" == i:
            sys.exit("Error !!, remove foward or Back slash from FILE_NAME")

    os.chdir(FOLDER_PATH)   
    print(os.getcwd())      #displays current working directory
    global COUNT 
    COUNT = 2815
    
    # Function to increment count 
    # to make the files sorted.
    def increment():
        global COUNT
        COUNT = COUNT + 1
    

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f) 
        f_name = FILE_NAME + str(COUNT)  
        increment()
        
        new_name = '{} {}'.format(f_name, f_ext)
        os.rename(f, new_name)
        
    print("successfully renamed {} files".format(len(os.listdir())))

if __name__ == "__main__":
    main()