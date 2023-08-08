import os
import shutil

def use_media(dunderfile, relpath):
    webMediaPath = os.path.abspath(os.path.join(__file__, "..\\..\\view\\web\\media"))
    if not os.path.exists(webMediaPath):
        os.mkdir(webMediaPath)
    resourcePath = os.path.abspath(os.path.join(dunderfile, "..", relpath))
    resourceName = os.path.split(resourcePath)[1]
    shutil.copyfile(resourcePath, os.path.join(webMediaPath, resourceName))
