import os
import time
import shutil

def get_info(file):
    ctime = os.path.getctime(file)
    mtime = os.path.getmtime(file)
    atime = os.path.getatime(file)

    return ctime, mtime, atime

def print_info(file):
    ctime = time.ctime(os.path.getctime(file))
    mtime = time.ctime(os.path.getmtime(file))
    atime = time.ctime(os.path.getatime(file))

    print(f'filename: {file}\ncreate time: {ctime}, modified time: {mtime}, access time: {atime}\n')


def copy_file(file, dstdir):
    shutil.copy2(file, os.path.join(dstdir, os.path.basename(file)))

file1 = os.path.join('image', 'eggs.png')
file2 = os.path.join('from', 'eggs.png')

print_info(file1)
print_info(file2)

dstdir = 'to'
if not os.path.exists(dstdir):
    os.makedirs(dstdir)

copy_file(file2, dstdir)

print_info(os.path.join(dstdir, os.path.basename(file2)))

# if not os.path.exists("output.txt"):
# 	with open("output.txt", "w"):
# 		pass

# with open("output.txt", "a") as f:
# 	f.write(str(file_ctime))
# 	f.write('\n')
# 	f.write(str(file_ctime))
# 	f.write('\n\n')
