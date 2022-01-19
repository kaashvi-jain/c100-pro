import time
import calandar
import os
import shutil
path = ''
days=730
seconds=time.time()-(days*24*60*60)
if os path.exists(path):
    os.remove(path)
else:
    print("file not found")