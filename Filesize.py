total=0
import os, shutil
print('start')
dir = 'c:\\Users\\Venkat Sriramagiri\Desktop\pp'
dir2 = 'c:\\Users\\Venkat Sriramagiri\Desktop\pp2'
for root, dirs, files in os.walk(dir):
    for file in files:
        fullname = os.path.join(root,file)
        if ('qp' in file) and ('(' not in file):
            shutil.move(fullname,dir2)
        total=total+os.path.getsize(fullname)
print ('Total size = ' + str(total))
