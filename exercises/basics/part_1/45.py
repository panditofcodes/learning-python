from  os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('/home/student') if isfile(join('/home/students',f))]

print(files_list)
