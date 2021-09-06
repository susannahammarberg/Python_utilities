import os

newpath = r'C:\Users\Sanna\Documents\python_utilities\test_create_folder' 
if not os.path.exists(newpath):
    os.makedirs(newpath)