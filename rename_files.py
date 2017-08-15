import os
import re

curr_dir = os.getcwd()
# DEST_DIR = some_dir
print('Renaming files in directory:', curr_dir)

for dpath, dname, lstfiles in os.walk(curr_dir):
    for file in lstfiles:
        src = os.path.join(dpath, file)
        # print(src)
        fname, fext = os.path.splitext(file)
        if 'app' in fname:
            new_fname = 'app{:02d}{}'.format(int(re.findall('[\d]+', fname)[0]), fext)
            dest = os.path.join(dpath, new_fname)
            # print(dest)
            try:
                os.rename(src, dest)
            except Exception as e:
                print(e)
    print('Renaming successful')
