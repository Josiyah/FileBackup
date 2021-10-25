import os
import time
import shutil
path = "/Users/admin/desktop"

time.time()
os.path.exists(path)
os.walk(path)
print(os.path.join(path, "newFolder"))
ctime = os.stat(path).st_ctime

